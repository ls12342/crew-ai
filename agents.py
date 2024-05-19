from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch news related with searched topic',
            backstory="""As a digital sleuth, you scour the internet for the news about Trump being an alien.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and fact-check the information',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of news stories, making a report about being fake news or not.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )
