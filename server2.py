# server.py
from mcp.server.fastmcp import FastMCP
from rag2 import *

# Create an MCP server
mcp = FastMCP("MCP-RAG-app",
              host="127.0.0.1",
              port=8080,
              timeout=30)

@mcp.tool()
def faq_retrieval_tool(query: str) -> str:
    """Retrieve the most relevant documents from FAQ collection. 
    Use this tool when the user asks about F1 Racing.

    Input:
        query: str -> The user query to retrieve the most relevant documents

    Output:
        context: str -> most relevant documents retrieved from a vector DB
    """
    # check type of text
    if not isinstance(query, str):
        raise ValueError("query must be a string")
    
    searcher = SmartSearcher(VectorDatabase("f1_faq_collection"), EmbeddingGenerator(batch_size=32))
    response = searcher.find_similar_content(query)
    return response

@mcp.tool()
def free_web_search_tool(query: str) -> list[dict]:
    """
    Search the web for up-to-date information for free using DuckDuckGo.
    Use this tool when the user asks about a specific topic or question 
    that is not related to the FAQ domain.

    Input:
        query: str -> The user query to search for information

    Output:
        context: list[str] -> list of most relevant web search results
    """
    # check type of text
    if not isinstance(query, str):
        raise ValueError("query must be a string")
    
    from duckduckgo_search import DDGS
    
    with DDGS() as ddgs:
        # Returns a list of dictionaries with title, href, and body
        results = [r for r in ddgs.text(query, max_results=5)]
    return results

@mcp.tool()
def fetch_wikipedia_summary(topic: str) -> str:
    """
    Fetch a summary of a topic from Wikipedia.
    Use this tool for factual questions about historical events, companies, or people.
    
    Input:
        topic: str -> The subject to look up on Wikipedia
        
    Output:
        summary: str -> A short summary describing the topic
    """
    if not isinstance(topic, str):
        raise ValueError("topic must be a string")
        
    import wikipedia
    
    try:
        return wikipedia.summary(topic, sentences=5)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Topic is too broad. Did you mean one of these? {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"Could not find a Wikipedia page for '{topic}'."

if __name__ == "__main__":
    print("Starting MCP server at http://127.0.0.1:8080 on port 8080")
    mcp.run()