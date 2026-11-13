# Clinical Text Normalisation - model card (v1)

## Intended use
Normalisation of free-text clinical notes into the institute's controlled vocabulary.

## Training data
De-identified discharge summaries from three partner trusts, 2019-2024 (n=184,220).

## Evaluation
| Split | Precision | Recall | F1 |
|-------|-----------|--------|----|
| validation | 0.913 | 0.897 | 0.905 |
| held-out | 0.902 | 0.884 | 0.893 |

## Limitations
Rare abbreviations outside the controlled vocabulary are passed through unchanged.
