"""
Score a single Puppy Escape narrative recall transcript.

For each rubric item:
  - scoring_method=keyword : whole-word regex match in transcript.
  - scoring_method=llm     : Claude judges the criterion.
  - scoring_method=hybrid  : Claude must score 1 AND a keyword must match.
"""

import csv
import json
import re
from pathlib import Path

import anthropic


PROJECT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = PROJECT_DIR / "prompts"
NARRATIVE_PATH = PROJECT_DIR / "narrative" / "narrative_pe.txt"

PROMPT_TEMPLATE_PATH = PROMPTS_DIR / "pe_prompt.txt"
QUESTIONS_PATH       = PROMPTS_DIR / "pe_questions.csv"
EXAMPLE_1_PATH       = PROMPTS_DIR / "pe_example_1.txt"
EXAMPLE_2_PATH       = PROMPTS_DIR / "pe_example_2.txt"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8192


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def load_items():
    """Load scoring items from pe_questions.csv."""
    items = []
    with open(QUESTIONS_PATH, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            items.append({
                "id": int(row["id"]),
                "question": row["question"],
                "scoring_method": row["scoring_method"].strip().lower(),
                "keywords": [k.strip() for k in row["keywords"].split(";") if k.strip()],
                "category": row["category"],
                "event": row["event"],
                "weight": float(row["weight"]),
            })
    return items


### Keyword scoring (mirrors utils/speech/scoring.py:check_keywords) ###
def keyword_match(transcript, keywords):
    """True if any keyword/phrase appears as a whole-word match (case-insensitive)."""
    text = transcript.lower()
    return any(
        re.search(r"\b" + re.escape(kw.lower()) + r"\b", text)
        for kw in keywords
    )


### Prompt assembly ###
def build_questions_block(llm_items):
    """Render the question list passed to Claude (id + question text only)."""
    return "\n".join(f'{item["id"]},"{item["question"]}"' for item in llm_items)


def assemble_system_prompt(llm_items):
    template = read_text(PROMPT_TEMPLATE_PATH)
    return (
        template
        .replace("{story}",     read_text(NARRATIVE_PATH))
        .replace("{questions}", build_questions_block(llm_items))
        .replace("{example_1}", read_text(EXAMPLE_1_PATH))
        .replace("{example_2}", read_text(EXAMPLE_2_PATH))
    )


### LLM call ###
def call_llm(transcript, llm_items):
    """Send the LLM-scored question subset to Claude; return {id: 0|1}."""
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=0.5,
        system=assemble_system_prompt(llm_items),
        messages=[{"role": "user", "content": f'"{transcript}"'}],
    )

    raw = response.content[0].text
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    if not match:
        raise ValueError(f"Could not find JSON array in LLM response:\n{raw}")
    parsed = json.loads(match.group(0))

    return {int(entry["id"]): int(entry["score"]) for entry in parsed}


### Combine & report ###
def score_transcript(transcript):
    items = load_items()
    llm_items = [it for it in items if it["scoring_method"] in ("llm", "hybrid")]
    llm_scores = call_llm(transcript, llm_items)

    results = []
    for it in items:
        method = it["scoring_method"]
        kw_hit = keyword_match(transcript, it["keywords"]) if it["keywords"] else False

        if method == "keyword":
            score = int(kw_hit)
        elif method == "llm":
            score = llm_scores.get(it["id"], 0)
        elif method == "hybrid":
            score = int(llm_scores.get(it["id"], 0) == 1 and kw_hit)
        else:
            raise ValueError(f"Unknown scoring_method '{method}' for id={it['id']}")

        results.append({
            "id": it["id"],
            "method": method,
            "score": score,
            "weight": it["weight"],
            "points": score * it["weight"],
            "category": it["category"],
            "event": it["event"],
        })

    return results


### Demo ###
if __name__ == "__main__":
    transcript = (
        "Last weekend, Harry and Danielle were walking their dog Maddy in "
        "the park and ran into some old friends. They talked for a while "
        "and decided to go to dinner on Thursday at Luigi's. After they "
        "said goodbye they realized Maddy got off her leash. They searched "
        "the park calling her name. Eventually they found her under a "
        "bench playing with a stick."
    )

    results = score_transcript(transcript)
    total = sum(r["points"] for r in results)
    max_total = sum(r["weight"] for r in results)

    for r in results:
        print(f"Q{r['id']:>2} [{r['method']:>7}] score={r['score']} "
              f"× weight={r['weight']:>3} = {r['points']}")
    print(f"\nTotal: {total} / {max_total}")
