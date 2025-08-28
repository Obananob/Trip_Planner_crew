import os
from dotenv import load_dotenv
from textwrap import dedent
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from agents import TravelAgents
from tasks import TravelTasks

# Load environment variables
load_dotenv()

# Set API keys from .env
openai_key = os.getenv("OPENAI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

if not openai_key or not serper_key:
    raise EnvironmentError("Missing OPENAI_API_KEY or SERPER_API_KEY in .env file")

os.environ["OPENAI_API_KEY"] = openai_key
os.environ["SERPER_API_KEY"] = serper_key

# Main Crew class
class TripCrew:
    def __init__(self, origin, cities, date_range, interests, traveler_profile, traveler_interest):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests
        self.traveler_profile = traveler_profile
        self.traveler_interest = traveler_interest

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        # Initialize agents
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Create tasks
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            local_tour_guide,
            self.traveler_profile
        )

        gather_city_info = tasks.gather_city_info(
            city_selection_expert,
            self.cities,
            self.traveler_interest
        )

        # Assemble the crew
        crew = Crew(
            agents=[expert_travel_agent, local_tour_guide, city_selection_expert],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        return crew.kickoff()

# Entry point
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    origin = input("Enter your origin city: ")
    cities = input("Enter destination cities (comma-separated): ").split(",")
    date_range = input("Enter your travel date range: ")
    interests = input("Enter your travel interests: ")
    traveler_profile = input("Describe your traveler profile (e.g., budget, preferences): ")
    traveler_interest = input("What are your specific interests for this trip? ")

    crew = TripCrew(origin, cities, date_range, interests, traveler_profile, traveler_interest)
    result = crew.run()

    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)