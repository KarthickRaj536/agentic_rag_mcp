---

````markdown
# 🚀 Agentic RAG System using MCP

An **Agentic Retrieval-Augmented Generation (RAG)** application powered by the **Model Context Protocol (MCP)**, enabling seamless integration of custom AI tools inside the Cursor IDE.

---

## 📺 Demo & Walkthrough

🎥 Full walkthrough:  
https://youtube.com/@machinelearningplus

---

## 🧩 Tech Stack

- Python  
- Model Context Protocol (MCP)  
- Qdrant (Vector Database)  
- LlamaIndex  
- HuggingFace Embeddings  
- Bright Data (Web Search)  
- Cursor IDE  

---

## ⚙️ Setup Instructions

### 1️⃣ Start Qdrant (Vector Database)

```bash
docker run -p 6333:6333 -p 6334:6334 -v qdrant_storage:/qdrant/storage:z qdrant/qdrant
````

---

### 2️⃣ Setup Bright Data Account

1. Create a free account: [https://brightdata.com/](https://brightdata.com/)
2. Generate your credentials (email & password)
3. Add them inside `server2.py`

---

### 3️⃣ Configure MCP Server in Cursor

#### 📌 Find your `uv` path

**Mac / Linux**

```bash
which uv
```

**Windows**

```bash
where uv
```

---

#### 📌 Add MCP Server

Go to:
`Cursor → Settings → MCP Servers → Add New`

Add the following in `mcp.json`:

```json
{
  "mcpServers": {
    "mcpRAG": {
      "command": "path/to/uv",
      "args": [
        "--directory",
        "absolute/path/to/projectdir",
        "run",
        "server2.py"
      ]
    }
  }
}
```

---

## ✅ Expected Output

* MCP server status turns **green**
* Available tools:

  * `f1_faq_search_tool`
  * `bright_data_web_search_tool`

---

## 💬 Usage

1. Open Cursor Chat (`Ctrl + L`)
2. Ask queries like:

   * "Search F1 FAQs about pit stops"
   * "Get latest F1 news"
3. The agent will:

   * Retrieve context from Qdrant
   * Perform web search using Bright Data
   * Generate a response using LLM

---

## 🧠 How It Works

```
User Query
   ↓
MCP Agent
   ↓
Tool Selection
   ├── Vector Search (Qdrant)
   └── Web Search (Bright Data)
   ↓
Context Aggregation
   ↓
LLM Response
```

---

## 📌 Notes

* Ensure Docker is running before starting Qdrant
* Verify `uv` path is correct
* Do not commit credentials to GitHub

---

## ⭐ Future Improvements

* UI dashboard
* Multi-document ingestion
* Streaming responses
* Improved tool orchestration

---

