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
            max_iter=2
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and fact-check the information',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of news stories, making a report about being fake news or not.""",
            verbose=True,
            allow_delegation=False,
        )
        
    def compile_fact_check(self):
        return Agent(
            role='FactCheckCompiler',
            goal='Compile the analyzed fact check report in a format',
            backstory="""As the final architect of the fact checking agency, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation of the report. Make sure to follow
            fact check format guidelines and maintain consistency throughout.""",
            verbose=True,
        )
