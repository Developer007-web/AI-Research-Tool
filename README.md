# 🔬 AI Research Tool — MCP Server

An MCP (Model Context Protocol) server built with **FastMCP** that gives AI assistants like Claude the ability to search academic papers, fetch web content, and save research notes — all through natural conversation.

Deployed and hosted on **Render** via SSE transport.

---

## 🚀 Features

| Tool | Description |
|---|---|
| `search_papers` | Search arXiv for academic papers by keyword |
| `fetch_url` | Fetch and read content from any webpage |
| `save_note` | Save research notes as `.md` files locally |

---

## 🛠️ Tech Stack

- **Python** — core language
- **FastMCP** — MCP server framework
- **HTTPX** — async HTTP client for arXiv and URL fetching
- **Uvicorn** — ASGI server
- **SSE (Server-Sent Events)** — transport protocol for MCP
- **Render** — cloud deployment platform

---

## 📁 Project Structure

```
AI-Research-Tool/
├── server.py          # FastMCP server with all 3 tools
├── requirements.txt   # Python dependencies
├── render.yaml        # Render deployment config
└── notes/             # Auto-created folder for saved research notes
```

---

## ⚙️ Setup & Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Developer007-web/AI-Research-Tool.git
cd AI-Research-Tool
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the server**
```bash
python server.py
```

The server starts on `http://localhost:10000` using SSE transport.

---

## 🔌 Connect to Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "research-assistant": {
      "url": "http://localhost:10000/sse"
    }
  }
}
```

Or if using the deployed Render URL:
```json
{
  "mcpServers": {
    "research-assistant": {
      "url": "https://your-render-url.onrender.com/sse"
    }
  }
}
```

---

## 🧪 Example Usage

Once connected to Claude, you can say:

> *"Search for recent papers on transformer attention mechanisms"*

> *"Fetch and summarize this research paper: https://arxiv.org/abs/..."*

> *"Save a note titled 'attention-notes' with a summary of what we discussed"*

Claude will call the appropriate MCP tool automatically.

---

## ☁️ Deployment (Render)

This project includes a `render.yaml` for one-click deployment on [Render](https://render.com).

1. Push the repo to GitHub
2. Connect it to Render
3. Render will auto-detect `render.yaml` and deploy
4. Use the live SSE URL in Claude Desktop config

The server reads `PORT` from environment variables, defaulting to `10000`.

---

## 📦 Dependencies

```
fastmcp
httpx
uvicorn
```

---

## 👤 Author

**Aman Pratap Singh**  
[GitHub](https://github.com/Developer007-web) · [LinkedIn](https://linkedin.com/in/aman-pratap-singh) · [Portfolio](https://developer007-web.github.io)

---

## 📄 License

MIT License — feel free to use and modify.
