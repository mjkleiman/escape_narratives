# Puppy Escape Narrative Recall

This repository contains the **Puppy Escape (PE) narrative**, the **scoring criteria** used to evaluate participant recall, and the **prompts** used to score recall responses automatically with large language models and embedding-based methods.

The Puppy Escape narrative is a brief story-recall task designed for use in cognitive assessment. Participants hear (or read) the narrative, then provide an immediate free-recall response and, after a delay, a delayed free-recall response. Recall is scored against a structured rubric of story categories and events.

## Repository contents

| Path | Description |
|---|---|
| `narrative/` | The Puppy Escape narrative text and any associated stimulus materials |
| `scoring/` | Scoring criteria — category-level and event-level rubrics, with reference targets and acceptable paraphrases |
| `prompts/` | Prompts and prompt templates used for automated scoring (LLM judging, embedding-based matching, and word-level matching) |
| `LICENSE` | CC BY-NC 4.0 license text |
| `LICENSE-CLINICAL-EXCEPTION.md` | Clinical and Internal Digital Use Exception (see below) |

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

The contents of this repository are released under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**, with the Clinical and Internal Digital Use Exception described below.

Full license text: <https://creativecommons.org/licenses/by-nc/4.0/legalcode>

### Clinical and Internal Digital Use Exception to the CC BY-NC 4.0 License

> Notwithstanding the NonCommercial restrictions outlined in the accompanying CC BY-NC 4.0 license, the Licensor grants healthcare providers, clinics, and hospital systems the right to use, digitize, and integrate this material for the direct clinical assessment, diagnosis, and treatment of individual patients.
>
> **Permitted Digital Integration:** Healthcare entities are explicitly permitted to integrate, automate, or digitize this material into their internal Electronic Health Records (EHRs), internal scoring systems, or internally developed clinical applications, provided such integration is used exclusively by their own staff for patient care.
>
> **Strict Prohibition on Commercial Sale and Marketing:** This exception does not permit the commercialization of the material itself. It is strictly prohibited to integrate, incorporate, or bundle this material into any software, digital package, scoring system, application, or platform that is subsequently sold, licensed for a fee, syndicated, or commercially marketed to third parties. Any software vendor, developer, or entity wishing to integrate this material into a commercial product or marketable platform must obtain a separate commercial license from the Licensor.

In short:

- **Allowed without a separate license:** academic and non-commercial research use under CC BY-NC 4.0; routine clinical use and internal digitization by healthcare providers, clinics, and hospital systems for the care of their own patients.
- **Requires a separate commercial license:** inclusion in any product, platform, or service that is sold, licensed for a fee, syndicated, or otherwise commercially distributed to third parties.

For commercial licensing inquiries, please contact the University of Miami Office of Technology Transfer at techtransfer@miami.edu
