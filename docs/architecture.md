```mermaid
flowchart TD
    A[Customer Email]
    B[Email Classification Agent]

    C{Critical Issue?}

    D[Human Escalation]
    E[Normal Request]

    F[RAG Knowledge Base]
    G[Response Generator]
    H[Guardrail Check]
    I[Final Response]

    A --> B
    B --> C

    C -->|Yes| D
    C -->|No| E

    E --> F
    F --> G
    G --> H
    H --> I