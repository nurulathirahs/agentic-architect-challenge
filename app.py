"""
Email Classifier Agent - Main Application Entry Point
Orchestrates email reading, classification, escalation evaluation, and reply generation.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.classify_email import classify_email
from agents.escalation import check_escalation
from agents.generate_reply import generate_reply


def run_pipeline(email_path: str):
    """
    Runs the full email classification pipeline.
    """
    if not os.path.exists(email_path):
        print(f"Error: Email file not found at '{email_path}'")
        sys.exit(1)

    print("=" * 60)
    print("           EMAIL CLASSIFIER AGENT RUNNER")
    print("=" * 60)
    print(f"Reading email from: {email_path}\n")

    with open(email_path, "r", encoding="utf-8") as f:
        email_content = f.read()

    print("--- INCOMING EMAIL CONTENT ---")
    print(email_content.strip())
    print("-" * 60)

    # 1. Classify Email
    category = classify_email(email_content)
    print(f"\n[1] Classification Result : {category}")

    # 2. Check Escalation
    escalation_info = check_escalation(email_content)
    is_escalated = escalation_info["is_escalated"]
    priority = escalation_info["priority"]
    reasons = ", ".join(escalation_info["reasons"])

    print(f"[2] Escalation Required   : {is_escalated} (Priority: {priority})")
    print(f"    Reason(s)            : {reasons}")

    # 3. Generate Reply
    reply = generate_reply(email_content, category, escalation_info)

    print("\n[3] Generated Response:")
    print("=" * 60)
    print(reply)
    print("=" * 60)


    # 4. Guardrail Check
    final_response = check_response(reply)

    print("\n[4] Final Response After Guardrail:")
    print("=" * 60)
    print(final_response)
    print("=" * 60)


    return {
        "category": category,
        "escalation": escalation_info,
        "reply": final_response
    }


def main():
    # Default to sample_data/email1.txt if no command line argument provided
    default_email = os.path.join(
        os.path.dirname(__file__), "sample_data", "email1.txt"
    )
    email_path = sys.argv[1] if len(sys.argv) > 1 else default_email
    run_pipeline(email_path)


if __name__ == "__main__":
    main()
