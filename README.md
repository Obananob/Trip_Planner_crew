# 🧳 Trip Planner CrewAI

A modular AI-powered travel planner built with CrewAI and LangChain. It uses custom agents and tools to generate personalized 7-day itineraries, recommend cities, and gather local insights.

## 🚀 Features
- Intelligent city selection based on traveler profile
- Detailed 7-day itinerary generation
- Real-time internet search using Serper API
- Built-in calculator for budget and logistics
- Modular agent-task architecture

## 🧠 Agents
- **Expert Travel Agent**: Crafts full itineraries with packing tips
- **City Selection Expert**: Picks the best destination based on preferences
- **Local Tour Guide**: Provides insider info and cultural highlights

## 🛠 Tools
- **SearchTool**: Uses Serper API to fetch real-time travel info
- **CalculatorTool**: Evaluates math expressions for budgeting

## 📦 Setup
```bash
poetry install
poetry run python main.py