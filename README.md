# Email Classifier Agent

An intelligent, modular Email Classifier Agent built in Python. The system reads incoming customer emails, automatically classifies them into specific categories (`Refund`, `Billing`, `Technical`, or `General`), detects if human escalation is required (e.g., high urgency, supervisor requests, or compliance flags), queries a domain-specific knowledge base, and generates tailored automated email responses.

---

## 🌟 Features

- **Multi-Category Classification**: Automatically categorizes customer emails into `Refund`, `Billing`, `Technical`, or `General`.
- **Intelligent Escalation Detection**: Identifies urgency triggers, negative sentiment, manager intervention requests, and legal/compliance risks to route to human support teams.
- **Knowledge Base Retrieval**: Dynamically integrates relevant knowledge base documentation (`refund_policy.txt`, `billing_faq.txt`, `technical_faq.txt`) into response context.
- **Automated Response Generation**: Produces clear, professional customer support replies tailored to the query context.
- **Continuous Integration Ready**: Includes a pre-configured GitHub Actions workflow (`test.yml`) for automated pipeline testing on every commit.

---

## 📂 Folder Structure

```text
email-classifier-agent/
├── app.py                      # Main entry point orchestrating agent pipeline
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment configuration
├── README.md                   # Project documentation and usage guide
├── agents/
│   ├── classify_email.py       # Email classification agent
│   ├── escalation.py           # Human escalation detection 
│   ├── guardrail.py            # Sensitive information detection 
agent
│   └── generate_reply.py       # Knowledge-aware reply generation agent
├── knowledge/
│   ├── refund_policy.txt       # Policy guidelines for refund requests
│   ├── billing_faq.txt         # FAQs for payment & billing inquiries
│   └── technical_faq.txt       # Troubleshooting guide for technical issues
├── sample_data/
│   └── email1.txt              # Sample customer email
│   └── email2.txt              # Sample email guardrail
└── .github/
    └── workflows/
        └── test.yml            # GitHub Actions CI workflow
```

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8 or higher installed on your system.

### Step 1: Clone this repository
```bash
git clone https://github.com/username/agentic-architect-challenge.git
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Agent Pipeline
Execute the main application script:

```bash
python app.py
```

By default, `app.py` reads and processes `sample_data/email1.txt`.

### Processing Custom Email Files
You can pass any custom text email file path as an argument to `app.py`:

```bash
python app.py path/to/your_email.txt
```

---

## ⚙️ How It Works

1. **Email Ingestion**: `app.py` reads raw text content from the target email file in `sample_data/`.
2. **Classification**: `agents/classify_email.py` evaluates keywords and intent to assign a category (`Refund`, `Billing`, `Technical`, or `General`).
3. **Escalation Analysis**: `agents/escalation.py` scans for escalation signals (e.g., manager requests, legal threat terms, urgency markers).
4. **Reply Generation**: `agents/generate_reply.py` loads category-specific facts from `knowledge/` and formats a professional response.
