import pytest

from sentinel import severity_from_score


def test_severity_ranges():
    assert severity_from_score(0) == "low"
    assert severity_from_score(24.99) == "low"
    assert severity_from_score(25) == "medium"
    assert severity_from_score(49.99) == "medium"
    assert severity_from_score(50) == "high"
    assert severity_from_score(74.99) == "high"
    assert severity_from_score(75) == "critical"
    assert severity_from_score(100) == "critical"


def test_rejects_out_of_range_scores():
    with pytest.raises(ValueError):
        severity_from_score(-0.01)
    with pytest.raises(ValueError):
        severity_from_score(100.01)
