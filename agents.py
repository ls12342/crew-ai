from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def news_fetcher_agent(self, query):
        return Agent(
            role='NewsFetcher',
            goal=f'Fetch news and official documents about {query}',
            backstory="""As a digital sleuth, you scour the internet for the news and documents that will form the basis of the fact check.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            max_iter=5
        )

    def news_analyzer_agent(self, query):
        return Agent(
            role='NewsAnalyzer',
            goal=f"""Analyze data about ${
                query} and fact-check if the claim is true or false""",
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of  data making a report about being true or not.""",
            verbose=True,
            max_iter=5
        )

    def compile_fact_check(self):
        return Agent(
            role='FactCheckCompiler',
            goal='Compile the analyzed fact check report in a format',
            backstory="""As the final architect of the fact checking agency, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation of the report. Make sure to follow
            fact check format guidelines and maintain consistency throughout.""",
            verbose=True,
            max_iter=15
        )
