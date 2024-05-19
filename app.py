import os
import requests
import json
from crewai import Agent, Task, Crew
from crewai_tools import (
    WebsiteSearchTool
)

web_rag_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        # embedder=dict(
        #     provider="ollama", # or openai, ollama, ...
        #     config=dict(
        #         model="nomic-embed-text",
        #         task_type="retrieval_document",
        #         # title="Embeddings",
        #     ),
        # ),
    )
)

researcher = Agent(
    role="Researcher",
    goal="Gather and analyze news related to the new BYD electric car",
    verbose=True,
    backstory=(
        "The researcher agent, a specialized news researcher"
        "is tasked with gathering and analyzing news related to the searched topic."
        "the researcher will use the search news tool to gather news from the web"
        "it should analyze if the found news is related with the searched topic"
    ),
    tools=[web_rag_tool],
    delegate=False
)

analyzer = Agent(
    role="Analyzer",
    goal="Analyze gathered news to check if the searched topic is fake news",
    verbose=True,
    backstory=(
        "The Analyzer agent, a specialized to analyze various news articles to check if the searched topic is fake news"
        "It should only use news found by the researcher agent"
        "The Analyzer should also mention the source he used to make the decision"
    ),
    delegate=False
)

research_task = Task(
    description="Look for news related to the searched topic",
    expected_output="A list of news articles related to the searched topic",
    agent=researcher
)

analyze_task = Task(
    description="Analyze the gathered news to check if the searched topic is fake news",
    expected_output="An answer saying if it is fake news or not, the source and explanation used to make the decision",
    agent=analyzer
)

crew = Crew(
    agents=[researcher, analyzer],
    tasks=[research_task, analyze_task]
)

result = crew.kickoff()
print(result)