# Project 1: Self-Hosted RAG and Agentic AI Platform

## Current Status

**Phase:** Phase 0 (Setup and Learning) — in progress
**Last updated:** 2026-05-08

## Environment

- OS: Windows 11, WSL2
- Python: 3.14.2 (C:\Python314\python.exe)
- Ollama: running on WSL2, accessible from Windows at localhost:11434
- Models pulled: llama3.2, deepseek-r1:32b, llama3.3:70b, qwen3.5:27b, gemma4:31b, qwen3:32b, qwen3.5:35b-a3b
- GitHub CLI: installed (gh 2.92.0)
- GitHub repo: https://github.com/judelahage/self-hosted-rag-agentic-ai-platform
- IDE note: VS Code shows red underlines on imports (fastapi, pydantic) — cosmetic issue, code runs fine. Need to configure Python interpreter or set up venv

## Reference

Full project plan lives at: `z:\Summer-Project\Summer_AI_Infrastructure_Project_Plan.md`
Test script (not part of repo): `z:\Summer-Project\ask_model.py`

---

## Phase 0: Setup and Learning (Week 0)

- [x] Install Ollama on WSL2
- [x] Pull a small model (llama3.2)
- [x] Micro-task 1: Chat with model in terminal
- [x] Micro-task 2: Python script that sends a prompt and prints the answer (ask_model.py)
- [x] Create GitHub repo (self-hosted-rag-agentic-ai-platform)
- [x] Micro-task 3: FastAPI backend with /chat endpoint
- [ ] Install Node.js (needed for Next.js frontend)
- [ ] Micro-task 4: Next.js frontend with text box that talks to backend
- [ ] Test full loop: type question in browser -> backend -> Ollama -> answer displayed

## Phase 1: Document Upload and Parsing (Week 2)

- [ ] Micro-task 5: Upload a .txt file and display its contents
- [ ] Add /upload endpoint to backend
- [ ] Parse PDF, TXT, and Markdown files
- [ ] Store document metadata
- [ ] Display uploaded documents in frontend

## Phase 2: Chunking, Embeddings, Elasticsearch (Week 3)

- [ ] Micro-task 6: Split uploaded text into chunks (500-1000 chars, 100-200 overlap)
- [ ] Micro-task 7: Generate embeddings for chunks (sentence-transformers or Ollama embeddings)
- [ ] Micro-task 8: Run Elasticsearch with Docker
- [ ] Micro-task 9: Store chunks + embeddings in Elasticsearch
- [ ] Confirm chunks are searchable via Elasticsearch

## Phase 3: RAG Pipeline (Week 4)

- [ ] Micro-task 10: Ask a question, retrieve chunks, use them in the prompt
- [ ] Build /rag/query endpoint
- [ ] Embed user question -> retrieve top chunks -> build context prompt -> LLM answers
- [ ] Return answer + cited source chunks
- [ ] Show source chunks in frontend UI

## Phase 4: Retrieval Mode Comparison (Week 4-5)

- [ ] Add retrieval mode dropdown: keyword / vector / hybrid search
- [ ] Compare results across modes
- [ ] Show which chunks were retrieved for each mode

## Phase 5: Agentic Workflow (Week 5)

- [ ] Choose framework: LangGraph, LangChain, or CrewAI
- [ ] Build multi-step workflow: retrieve -> draft answer -> validate grounding -> revise -> return
- [ ] Add "agent mode" toggle in frontend
- [ ] Show agent trace/logs in UI

## Phase 6: Evaluation and Polish (Week 6)

- [ ] Create evaluation question set (questions.json)
- [ ] Run retrieval evaluation: keyword vs vector vs hybrid
- [ ] Record latency metrics
- [ ] Write evaluation report
- [ ] Dockerize the full app (docker-compose.yml)
- [ ] Record demo video
- [ ] Polish README with architecture diagram, screenshots, setup instructions
- [ ] Write final resume bullets

## Advanced Features (stretch goals, after MVP)

- [ ] Source confidence scores
- [ ] Document collections (group by project)
- [ ] RAG evaluation dashboard (latency, chunk count, correct chunk found)
- [ ] Resume bullet generator agent

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Next.js + TypeScript |
| Backend | FastAPI + Python |
| LLM Runtime | Ollama |
| Embeddings | sentence-transformers or Ollama |
| Vector DB | Elasticsearch |
| RAG Framework | Haystack or LangChain |
| Agent Layer | LangGraph or CrewAI |
| Containers | Docker (later) |

## Folder Structure

```
self-hosted-rag-agentic-ai-platform/
  README.md
  PROGRESS.md          <-- you are here
  .gitignore
  backend/
    requirements.txt
    app/
      main.py          -- FastAPI app, CORS, health check
      routes/
        chat.py        -- /chat endpoint, calls Ollama
      services/        -- (empty, will hold llm_service, elasticsearch_service, etc.)
  frontend/            -- (not created yet)
  docker/              -- (not created yet)
  eval/                -- (not created yet)
  docs/                -- (not created yet)
```
