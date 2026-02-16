# Project Roadmap: The Syllabus Strategist

**Goal**: Build an autonomous agent that ingests course syllabi (PDFs), understands your schedule (Calendar), and acts as a personal academic concierge to optimize your time and grades.

**Repo Name Suggestion**: `syllabus-strategist` or `academic-agent`

---

## Phase 1: Foundations & Reasoning (Weeks 1–4)
**Focus**: Building the "Brain" and Data Ingestion.

*   **Week 2 (Reasoning & Prompting)**:
    *   **Feature**: "The Deadline Extractor".
    *   **Task**: Build a script using `openai` or `anthropic` API.
    *   **Prompt Engineering**: Use Chain-of-Thought (CoT) to parse messy PDF text into structured JSON `{"assignment": "Midterm", "date": "2026-03-12", "weight": "20%"}`.
    *   **Challenge**: Handling ambiguous dates ("Due Week 5").
*   **Week 3 (Developer Stack)**:
    *   **Architecture**: Set up the project structure.
    *   **Decision**: **PydanticAI** (perfect for structured data extraction) vs **LangGraph** (workflow optimization). *Recommendation: Use PydanticAI for the extractor agents and LangGraph for the overall "Planning" workflow.*
    *   **Deliverable**: A CLI tool that takes a PDF path and outputs a clean schedule CSV.
*   **Week 4 (Knowledge Representation)**:
    *   **Feature**: "The Context Vault".
    *   **Tech**: efficient embeddings (e.g., `text-embedding-3-small`) stored in a local Vector DB (ChromaDB or LanceDB).
    *   **Goal**: Query "What is the reading for the Ethics module?" and get the exact paragraph from the syllabus.

## Phase 2: Knowledge Augmentation (Weeks 5–7)
**Focus**: Connecting the dots between courses.

*   **Week 5 (RAG 2.0)**:
    *   **Feature**: "Smart Search".
    *   **Task**: Implement Hybrid Search (Keyword + Semantic). Address query rewriting: "When is the big paper due?" -> "Find assignments with weight > 20%".
*   **Week 6 (GraphRAG)**:
    *   **Feature**: "The Knowledge Graph".
    *   **Tech**: **Neo4j** (Local Docker container).
    *   **Goal**: Map concepts. Nodes: `Concept`, `Assignment`, `Date`. Edges: `RELATES_TO`, `DUE_ON`.
    *   **Unlock**: "Show me all assignments that require knowledge of 'Transformers' across all my classes."
*   **Week 7 (Evaluation)**:
    *   **Feature**: "The Grader".
    *   **Tech**: **RAGAS** framework.
    *   **Task**: Create a test set of 20 questions ("When is the final?", "What is the late policy?"). Measure the agent's accuracy in retrieving the right answer from the syllabus.

## Phase 3: The Agentic Shift & MCP (Weeks 8–11)
**Focus**: *Doing* things, not just reading things. **Crucial Phase.**

*   **Week 8 & 9 (MCP Server)**:
    *   **Feature**: "The Calendar Bridge".
    *   **Task**: Build a custom **MCP Server** (`syllabus-mcp`).
    *   **Tools**:
        *   `list_calendar_events(start, end)`: Read your real GCal/iCal.
        *   `create_study_block(title, start, end)`: Actually block time on your calendar.
    *   **Integration**: The LLM can now *see* your dentist appointment and *schedule* study time around it.
*   **Week 10 (Multi-Agent Workflows)**:
    *   **Feature**: " The Council".
    *   **Agents**:
        *   *Extractor*: Reads PDFs.
        *   *Scheduler*: Manages time slots.
        *   *Critic*: specific "Professor Persona" that critiques your plan ("You only allocated 2 hours for a 30% project? Unwise.").
*   **Week 11 (Memory)**:
    *   **Feature**: "User Preferences".
    *   **Task**: Store user facts ("I hate mornings", "I create better work on weekends") in a SQLite DB. The Scheduler agent MUST respect these constraints.

## Phase 4: Scale & Governance (Weeks 12–14)
**Focus**: Optimization and Polish.

*   **Week 12 (Small Models)**:
    *   **Task**: Switch the "Extractor" agent to use a smaller, cheaper model (e.g., Llama 3 running locally via Ollama) to save money/tokens.
*   **Week 13 (Fine-tuning)**:
    *   **Task**: (Optional) Fine-tune a small model on your specific way of describing tasks.
*   **Week 14 (Safety)**:
    *   **Task**: Guardrails. Ensure the agent doesn't delete important calendar events or hallucinate due dates.

## Phase 5: Capstone Showcase (Week 15)
**Deliverable**: A polished, local web-app (Streamlit or NiceGUI) where you upload a PDF, sync your calendar, and it generates a "Semester Survival Plan" automatically.

---

## Technical Stack Recommendation
*   **Language**: Python 3.11+
*   **LLM Interface**: `litellm` (for swapping models easily) or `pydantic-ai`.
*   **Database**: `LanceDB` (Vector) + `SQLite` (Metadata/Memory) + `Neo4j` (Graph - Optional but required for Week 6).
*   **MCP**: `mcp` python SDK.
*   **Frontend**: `Streamlit` (Fastest for data apps) or `Next.js` (if you want to show off web dev skills). *Stick to Streamlit for this class to focus on the AI backend.*
