"""Render the clinical text normalisation model card."""

from pathlib import Path

TEMPLATE = """# Clinical Text Normalisation - model card ({version})

## Intended use
{intended_use}

## Evaluation
{metrics}
"""


def render(version, intended_use, metrics, out_path):
    body = TEMPLATE.format(version=version, intended_use=intended_use, metrics=metrics)
    Path(out_path).write_text(body, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    render("v1", "Normalisation of free-text clinical notes.", "F1 0.893", "model_card.md")
