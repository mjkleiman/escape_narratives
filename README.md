# Escape Narratives for Narrative Recall Assessment

This repository contains the **Puppy Escape** narrative, the **scoring criteria** used to evaluate participant recall, and the **prompts** used to score recall responses automatically with large language models and embedding-based methods.

The Escape narratives are brief story-recall narratives designed for use in narrative recall cognitive assessment. Participants are visually shown *and* verbally read the narrative. They are then asked to provide an immediate free-recall response, and after a 15-20 minute delay, a delayed free-recall response. Recall is scored against a structured rubric of story categories and events. Manual scoring is aided by a reduced 18-item rubric, which scores only content units shown to be most useful at identifying early-stage impairment.

## Repository contents

| Path | Description |
|---|---|
| `puppy_escape/narrative/` | The Puppy Escape narrative text and any associated stimulus materials |
| `puppy_escape/scoring/` | Puppy Escape scoring criteria — category-level and event-level rubrics, with reference targets and acceptable paraphrases |
| `puppy_escape/prompts/` | Puppy Escape prompts and prompt templates used for automated scoring (LLM judging, embedding-based matching, and word-level matching) |
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

>### Clinical, Research, and Internal Digital Use Exception to the CC BY-NC 4.0 License
>
>Notwithstanding the NonCommercial restrictions outlined in the accompanying CC BY-NC 4.0 license, the Licensor grants the following permissions:
>
>#### Clinical Use
>
>Healthcare providers, clinics, and hospital systems are granted the right to use, digitize, and integrate this material for the direct clinical assessment, diagnosis, and treatment of individual patients.
>
>#### Research Use
>
>Academic institutions, non-profit research organizations, contract research organizations (CROs), pharmaceutical and biotechnology companies, and other entities are granted the right to use this material for research purposes, including in clinical trials, observational studies, and other investigations, regardless of the funding source (including industry-sponsored research). This permission extends to the digitization and integration of the material into research data collection systems, electronic data capture (EDC) platforms, and internal research applications used by the sponsoring entity and its research collaborators.
>
>#### Permitted Digital Integration
>
>Healthcare and research entities are explicitly permitted to integrate, automate, or digitize this material into their internal Electronic Health Records (EHRs), internal scoring systems, electronic data capture systems, or internally developed clinical or research applications, provided such integration is used exclusively by their own staff and authorized collaborators for patient care or research.
>
>#### Strict Prohibition on Commercial Sale and Marketing 
>
>This exception does not permit the commercialization of the material itself. It is strictly prohibited to integrate, incorporate, or bundle this material into any software, digital package, scoring system, application, or platform that is subsequently sold, licensed for a fee, syndicated, or commercially marketed to third parties. Any software vendor, developer, or entity wishing to integrate this material into a commercial product or marketable platform must obtain a separate commercial license from the Licensor.

In short:

- **Allowed without a separate license:** academic and research use under CC BY-NC 4.0; routine clinical use and internal digitization by research entities, healthcare providers, clinics, and hospital systems for internal use and the care of their own patients.
- **Requires a separate commercial license:** inclusion in any product, platform, or service that is sold, licensed for a fee, syndicated, or otherwise commercially distributed to third parties.

## Commercial Licensing

The Escape Narratives scoring criteria are owned by the University of Miami. 
For commercial licensing inquiries regarding the scoring criteria, please 
contact the University of Miami Office of Technology Transfer at 
techtransfer@miami.edu.

## Copyright

Puppy Escape Narrative © 2016-2026 Michael J. Kleiman. 

Puppy Escape scoring criteria © 2026 University of Miami.