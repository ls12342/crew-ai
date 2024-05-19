from datetime import datetime
from crewai import Task

class AINewsLetterTasks():
    def fetch_news_task(self, agent, query):
        return Task(
            description=f'Fetch relevant news and official documents about {query}',
            agent=agent,
            expected_output=f"Data about ${query}, URLs, and a brief summary."
        )

    def analyze_news_task(self, agent, context, query):
        return Task(
            description=f'Analyze each news story check if they confirm if the claim ${query} is true or false',
            agent=agent,
            context=context,
            expected_output="An analysis for each news and documents, bringing all the data and the URL of the source of the information.") 

    def compile_fact_check_task(self, agent, context):
        return Task(
            description='Compile the fact check',
            agent=agent,
            context=context,
            expected_output="""A complete report in markdown format, with a consistent style and layout.
                Example Output: 
                '# Is trump an alien?:\\n\\n
                This claim is false
              
                ## Why this claim is false\\n\\n
                This claim is false because there is no evidence to support this claim.\\n\\n
                ## Sources\\n\\n
                [CNN](https://www.cnn.com)\\n\\n
                [BBC](https://www.bbc.com)\\n\\n
            """,
        )
        