from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent, query):
        return Task(
            description=f"""Fetch relevant news and official documents about {
                query}""",
            agent=agent,
            expected_output=f"Data about ${query}, URLs, and a brief summary."
        )

    def analyze_news_task(self, agent, context, query):
        return Task(
            description=f"""Analyze each news story check if they confirm if the claim ${
                query} is true or false""",
            agent=agent,
            context=context,
            expected_output="An analysis for each news and documents, bringing all the data and the URL of the source of the information.")

    def compile_fact_check_task(self, agent, context, query):
        return Task(
            description='Compile the fact check',
            agent=agent,
            context=context,
            expected_output="A complete report about ${query} explaining and showing resources and data about the fact check. The final report should include if the claim is true or false. A claim can also be not confirmed",
        )
