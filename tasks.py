from datetime import datetime
from crewai import Task

class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch news related with trump being an alien',
            agent=agent,
            expected_output="""Fetch news related with trump being an alien, URLs, and a brief summary. 
                Example Output: 
                [
                    {  'title': 'Trump goes to the hospital', 
                    'url': 'https://example.com/story1', 
                    'summary': 'Trump is not an alien'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story check if they confirm if the claim (trump is an alien) is true or false',
            agent=agent,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. 
                Example Output: 
                '## Trump goes to the hospital\n\n
                **The Rundown:
                ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                **The details:**\n\n
                - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                **Why it matters:** While AI-related ads have been rampant over the last year, its Super Bowl presence is a big mainstream moment.\n\n'
            """
        )

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