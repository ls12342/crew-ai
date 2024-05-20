
from langchain_community.vectorstores import LanceDB
from langchain.tools import tool


class GetData:
    @tool("Get Data Tool")
    def data(query: str) -> str:
        """Search LanceDB for relevant news information based on a query."""
        vectorstore = LanceDB(embedding=embedding_function, connection=table)
        retriever = vectorstore.similarity_search(query)
        return retriever
