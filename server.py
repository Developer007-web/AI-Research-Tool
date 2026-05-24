from fastmcp import FastMCP
import httpx

mcp = FastMCP("Research Assistant 🔬")

# Tool 1: Search arXiv for papers
@mcp.tool
async def search_papers(query: str, max_results: int = 5) -> str:
    """Search arXiv for academic papers by keyword."""
    url = f"https://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    return resp.text  # Returns XML with paper titles, abstracts, links

# Tool 2: Fetch and read a web page
@mcp.tool
async def fetch_url(url: str) -> str:
    """Fetch and return the text content of any URL."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, follow_redirects=True)
    return resp.text[:5000]  # Return first 5000 chars

# Tool 3: Save research notes
@mcp.tool
def save_note(title: str, content: str) -> str:
    """Save a research note to a local file."""
    with open(f"notes/{title}.md", "w") as f:
        f.write(content)
    return f"Note '{title}' saved."

if __name__ == "__main__":
    mcp.run()