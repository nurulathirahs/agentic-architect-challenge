"""
Generate Reply Agent
Retrieves relevant knowledge base content and generates a professional email reply.
"""

import os
from typing import Any, Dict

KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge")

KNOWLEDGE_FILES = {
    "Refund": "refund_policy.txt",
    "Billing": "billing_faq.txt",
    "Technical": "technical_faq.txt",
}


def load_knowledge(category: str) -> str:
    """
    Loads text content from the knowledge base directory for a given category.
    """
    filename = KNOWLEDGE_FILES.get(category)
    if not filename:
        return "General support guidelines apply."

    filepath = os.path.join(KNOWLEDGE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return "Knowledge base entry not found."


def generate_reply(
    email_text: str, category: str, escalation_info: Dict[str, Any]
) -> str:
    """
    Generates a context-aware customer support email response.
    """
    knowledge = load_knowledge(category)
    is_escalated = escalation_info.get("is_escalated", False)

    reply_lines = [
        "Dear Customer,",
        "",
        "Thank you for contacting our support team.",
    ]

    if is_escalated:
        reply_lines.append(
            "Please note: Your message has been marked with HIGH PRIORITY and escalated to our Tier 2 Support Team & Management. "
            "A senior specialist will personally follow up with you shortly."
        )
        reply_lines.append("")

    if category == "Refund":
        reply_lines.append(
            "Regarding your refund inquiry: Subscriptions are eligible for a full refund within 30 days of purchase. "
            "Refunds are credited back to your original payment method within 3 to 5 business days."
        )
    elif category == "Billing":
        reply_lines.append(
            "Regarding your billing inquiry: You can update payment details and download PDF invoices directly "
            "from your Account Dashboard under Settings > Billing."
        )
    elif category == "Technical":
        reply_lines.append(
            "Regarding your technical request: Please try clearing browser cache/cookies or resetting your password. "
            "You can also check system status updates at status.example.com."
        )
    else:
        reply_lines.append(
            "We have logged your request and our support team is currently reviewing your message."
        )

    reply_lines.extend(
        [
            "",
            "[Relevant Knowledge Base Excerpt]",
            "---------------------------------",
            knowledge.strip()[:350] + ("..." if len(knowledge) > 350 else ""),
            "",
            "Best regards,",
            "Customer Support Agent",
            "AI Assistant Suite",
        ]
    )

    return "\n".join(reply_lines)


if __name__ == "__main__":
    esc = {"is_escalated": True, "reasons": ["Manager requested"]}
    print(generate_reply("Refund please", "Refund", esc))
