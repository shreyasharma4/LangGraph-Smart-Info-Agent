# LangGraph Weather Agent

A simple conversational agent built using LangGraph that provides real-time weather updates for any city in the world.

---

## Features
- Developed using [LangGraph](https://python.langchain.com/docs/langgraph)
- Fetches live weather information from [wttr.in](https://wttr.in/)
- Works globally with accurate city-based data
- Cross-platform support that runs on Windows, macOS, and Linux

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/smart_info_agent_langgraph.git
cd smart_info_agent_langgraph

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the agent
python weather_agent.py

# You can then interact with the agent in the terminal by typing:
# You: what's the weather in noida?
# Agent: Haze, 25°C in Noida.
