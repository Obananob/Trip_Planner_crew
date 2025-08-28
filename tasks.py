from crewai import Task
from textwrap import dedent

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            agent=agent,
            description=dedent(
                f"""
                **Task:** Plan a detailed 7-day travel itinerary  
                **Description:** Expand the city guide into a full 7-day itinerary, including daily activities, dining options, and travel tips.  
                You MUST suggest actual places to visit, eat, and stay.  
                This itinerary should cover all aspects of the trip, from arrival to departure, integrating the city guide information with practical travel logistics.

                **Parameters**:  
                - City: {city}  
                - Trip Date: {travel_dates}  
                - Traveler Interests: {interests}  

                **Note**: {self.__tip_section()}
                """
            ),
            expected_output="A fully detailed 7-day itinerary featuring daily activities, dining spots, accommodations, and travel logistics tailored to the traveler's interests."
        )

    def identify_city(self, agent, traveler_profile):
        return Task(
            agent=agent,
            description=dedent(
                f"""
                **Task:** Identify the most suitable travel destination  
                **Description:** Based on the traveler's profile—including preferences, budget, travel history, and seasonal considerations—recommend a city that best aligns with their interests and constraints.  
                You MUST justify your choice with clear reasoning, referencing climate, accessibility, safety, and cultural fit.

                **Parameters**:  
                - Traveler Profile: {traveler_profile}  

                **Note**: {self.__tip_section()}
                """
            ),
            expected_output="A single recommended city with rationale and brief highlights"
        )

    def gather_city_info(self, agent, city, traveler_interests):
        return Task(
            agent=agent,
            description=dedent(
                f"""
                **Task:** Gather comprehensive travel information for a selected city  
                **Description:** Compile relevant and up-to-date details about the city, including top attractions, local cuisine, neighborhoods, transportation options, safety tips, and cultural norms.  
                Tailor the information to match the traveler's interests.  
                You MUST include real places, local customs, and practical advice.

                **Parameters**:  
                - City: {city}  
                - Traveler Interests: {traveler_interests}  

                **Note**: {self.__tip_section()}
                """
            ),
            expected_output="A structured city guide tailored to the traveler's interests"
        )