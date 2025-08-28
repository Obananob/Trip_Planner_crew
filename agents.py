from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTool
from tools.calculator_tools import CalculatorTool

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""Expert in Travel Planning and Logistics. I have decades of experience making travel itineraries."""),
            goal=dedent("""Create a detailed itinerary for a 7-day travel plan, including daily activities, packing suggestions, and travel tips."""),
            tools=[SearchTool(), CalculatorTool()],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""Expert at analyzing travel data to pick ideal destinations based on weather, budget, and activities."""),
            goal=dedent("""Select the best city for the traveler based on their preferences and constraints."""),
            tools=[SearchTool()],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""Knowledgeable local guide with extensive insights into cities and their attractions."""),
            goal=dedent("""Provide the best insider tips and cultural highlights for the selected city."""),
            tools=[SearchTool()],
            verbose=True,
            llm=self.OpenAIGPT35,
        )