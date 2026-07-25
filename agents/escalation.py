"""
Escalation Agent
Evaluates whether an email requires human escalation based on urgency,
negative sentiment, legal threats, or explicit escalation requests.
"""

import re
from typing import Any, Dict


def check_escalation(email_text: str) -> Dict[str, Any]:
    """
    Checks if an email requires human escalation.
    Returns a dictionary containing escalation status, priority, and reasons.
    """
    text_lower = email_text.lower()
    reasons = []

    # Check for explicit manager or human intervention requests
    if re.search(
        r"\b(manager|supervisor|speak with a manager|speak to a manager|human|escalate|tier 2)\b",
        text_lower,
    ):
        reasons.append("Explicit request for manager or supervisor intervention")

    # Check for legal, financial, or regulatory threats
    if re.search(
        r"\b(lawyer|attorney|legal|sue|lawsuit|bbb|better business bureau|fraud|police)\b",
        text_lower,
    ):
        reasons.append("Potential legal or compliance threat detected")

    # Check high urgency or strong negative emotion
    if re.search(
        r"\b(urgent|immediately|asap|furious|unacceptable|disaster|terrible service)\b",
        text_lower,
    ):
        reasons.append("High urgency or severe negative sentiment expressed")

    is_escalated = len(reasons) > 0

    return {
        "is_escalated": is_escalated,
        "reasons": reasons if is_escalated else ["Standard automated processing"],
        "priority": "HIGH" if is_escalated else "NORMAL",
    }


if __name__ == "__main__":
    sample = "If this is not fixed immediately I will speak to your manager!"
    print(check_escalation(sample))
