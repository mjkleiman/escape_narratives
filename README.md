# Escape Narratives for Narrative Recall Assessment

This repository contains the **Puppy Escape** narrative, the **scoring criteria** used to evaluate participant recall, and the **prompts** used to score recall responses automatically with large language models and embedding-based methods.

The Escape narratives are brief story-recall narratives designed for use in narrative recall cognitive assessment. Participants are visually shown *and* verbally read the narrative. They are then asked to provide an immediate free-recall response, and after a 15-20 minute delay, a delayed free-recall response. Recall is scored against a structured rubric of story categories and events. Manual scoring is aided by a reduced 18-item rubric, which scores only content units shown to be most useful at identifying early-stage impairment.

## Repository contents

| Path | Description |
|---|---|
| `puppy_escape/narrative/` | The Puppy Escape narrative text and any associated stimulus materials |
| `puppy_escape/scoring/` | Puppy Escape scoring criteria — category-level and event-level rubrics, with reference targets and acceptable paraphrases |
| `puppy_escape/prompts/` | Puppy Escape prompts and prompt templates used for automated scoring (LLM judging, embedding-based matching, and word-level matching) |
| `LICENSE.pdf` | License text |

## Scoring overview

Responses are scored along two complementary dimensions:

- **Category scores** — higher-level units of meaning (e.g., setting, characters, key plot beats) that capture gist-level recall.
- **Event scores** — finer-grained propositions within each category that capture specific recalled details.

Automated scoring combines three signals:

1. **LLM judging** — a model is prompted with the rubric and the participant response and asked to mark which categories/events are recalled, including paraphrases.
2. **Word matching** — surface-level lexical matches against verbatim cue words.

The exact prompts, targets, and thresholds used in each step are provided in `prompts/` and `scoring/`.

## Intended use

These materials are intended for research and clinical assessment of memory and narrative recall. They are not a diagnostic instrument on their own and should be interpreted alongside other clinical information.

## Citation

If you use the narrative, scoring criteria, or prompts in published work, please cite this repository. A formal citation entry will be added once the associated manuscript is published.

## License

The contents of this repository are released under a Non-Exclusive Copyright License Agreement jointly granted by Dr Michael Kleiman and the University of Miami.

You must request access using our web form before use: https://umiamibrainhealth.org/escape-narratives/

- **Allowed without a separate license:** academic and research use, routine clinical use by healthcare providers, clinics, research entities, and hospital systems for internal use and the care of their own patients. Fee-for-service clinical use is permitted.
- **Requires a separate commercial license:** inclusion in any product, platform, or service that is sold, licensed for a fee, syndicated, or otherwise commercially distributed to third parties.

## Commercial Licensing

The Escape Narratives scoring criteria are owned by the University of Miami. For commercial licensing inquiries regarding the use of the narrative and scoring criteria, please submit a request at https://umiamibrainhealth.org/escape-narratives/

## Copyright

Puppy Escape Narrative © 2015-2026 Michael J. Kleiman. 

Puppy Escape scoring criteria © 2026 University of Miami.
