from fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("Research Assistant 🔬")


@mcp.tool
async def search_papers(query: str, max_results: int = 5) -> str:
    """Search arXiv papers."""

    url = f"https://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

    return resp.text


@mcp.tool
async def fetch_url(url: str) -> str:
    """Fetch webpage content."""

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, follow_redirects=True)

    return resp.text[:5000]


@mcp.tool
def save_note(title: str, content: str) -> str:
    """Save research notes."""

    os.makedirs("notes", exist_ok=True)

    with open(f"notes/{title}.md", "w", encoding="utf-8") as f:
        f.write(content)

    return f"Saved: {title}"


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port
    )
