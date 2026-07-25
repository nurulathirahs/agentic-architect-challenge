"""
Email Classification Agent
Classifies input email text into one of four categories:
- Refund
- Billing
- Technical
- General
"""

import os
import re

VALID_CATEGORIES = ["Refund", "Billing", "Technical", "General"]


def classify_email(email_text: str) -> str:
    """
    Classifies email text into Refund, Billing, Technical, or General.
    Analyzes keywords, intent patterns, and semantic structure.
    """
    text_lower = email_text.lower()

    # Keyword and intent pattern matching scores
    refund_score = len(
        re.findall(
            r"\b(refund|money back|return|cancel order|reimburse|reimbursement)\b",
            text_lower,
        )
    )
    billing_score = len(
        re.findall(
            r"\b(billing|invoice|credit card|charge|payment|subscription fee|receipt)\b",
            text_lower,
        )
    )
    technical_score = len(
        re.findall(
            r"\b(error|bug|crash|login|password|issue|broken|system|technical|code|timeout|500)\b",
            text_lower,
        )
    )

    scores = {
        "Refund": refund_score,
        "Billing": billing_score,
        "Technical": technical_score,
    }

    max_category = max(scores, key=scores.get)
    if scores[max_category] > 0:
        return max_category

    return "General"


if __name__ == "__main__":
    sample = "I want a refund for my order #12345."
    print("Classified as:", classify_email(sample))
