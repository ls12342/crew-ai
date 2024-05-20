from typing import Union
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from tools.search_news import SearchNewsDB
from tools.get_data import GetData
from langchain_community.tools import DuckDuckGoSearchRun


@CrewBase
class FactCheckCrew():
    """FactCheckCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, api: Union[str, None] = None, model: str = None) -> None:
        self.api = api
        self.model = model
        if self.api == "GROQ":
            self.groq_llm = ChatGroq(temperature=0, model_name=self.model)
        elif self.api == "OLLAMA":
            self.groq_llm = ChatOpenAI(
                model=model,
                base_url="http://localhost:11434/v1"
            )

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['data_researcher'],
            groq_llm=self.groq_llm,
            tools=[SearchNewsDB().news],
        )

    @agent
    def company_analyst(self) -> Agent:
        search_tool = DuckDuckGoSearchRun()
        return Agent(
            config=self.agents_config['data_analyst'],
            groq_llm=self.groq_llm,
            tools=[GetData().data, search_tool],
        )

    @task
    def research_fact_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_fact_data_task'],
            agent=self.company_researcher()
        )

    @task
    def data_analyst(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_fact_data_task'],
            agent=self.company_analyst()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # process=Process.hierarchical,
            # manager_llm=self.groq_llm,
            verbose=2
        )
