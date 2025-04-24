from langchain_google_community import GoogleSearchAPIWrapper
from langchain.tools import Tool


search = GoogleSearchAPIWrapper()

def top5_results(query):
    results = search.results(query, 5)
    return results

def create_google_search_tool():
    tool = Tool(
        name="google_search",
        description="Realiza pesquisa no Google e retorna os cinco resultados mais relevantes detalhadamente.",
        func=top5_results,
    )
    return tool
