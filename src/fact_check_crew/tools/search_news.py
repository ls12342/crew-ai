import requests
import os
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import LanceDB
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fact_check_crew.db import lanceDBConnection


class SearchDataDB:
    @tool("Data DB Tool")
    def data(query: str):
        """Fetch data and process their contents"""
        print("Query:", query)

        API_KEY = os.getenv(
            'NEWSAPI_KEY')  # Fetch API key from environment variable
        base_url = f"httpsp://newsapi.org/v2/everything?q=stock${query}"

        params = {
            'sortBy': 'publishedAt',
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 15,
        }

        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            return "Failed to retrieve news."

        articles = response.json().get('articles', [])
        all_splits = []
        for article in articles:
            print("article", article)
            # Assuming WebBaseLoader can handle a list of URLs
            loader = WebBaseLoader(article['url'])
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            all_splits.extend(splits)  # Accumulate splits from all articles

        # Index the accumulated content splits if there are any
        if all_splits:
            embedding_function = OllamaEmbeddings(model="nomic-embed-text")
            # LanceDB as vector store
            emb = embedding_function.embed_query("hello_world")
            dataset = [{"vector": emb, "text": "dummy_text"}]
            table = lanceDBConnection(dataset)
            vectorstore = LanceDB.from_documents(
                all_splits, embedding=embedding_function, connection=table)
            retriever = vectorstore.similarity_search(query)
            return retriever
        else:
            return "No content available for processing."
