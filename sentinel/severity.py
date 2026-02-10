"""Severity mapping helpers.

The core logic maps a score in the 0..100 range to a severity band.
"""

from __future__ import annotations


def severity_from_score(score: float) -> str:
    """Return a severity label for a score between 0 and 100.

    Bands:
    - 0-24.99: low
    - 25-49.99: medium
    - 50-74.99: high
    - 75-100: critical

    Raises:
        ValueError: if score is outside 0..100.
    """
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    # Bug fix: inclusive upper bound avoids classifying 100 incorrectly.
    if score < 25:
        return "low"
    if score < 50:
        return "medium"
    if score < 75:
        return "high"
    return "critical"
