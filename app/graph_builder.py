from langgraph.graph import StateGraph
from .state import AgentState
from .nodes import intent_node

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("Intent", intent_node)
    graph.set_entry_point("Intent")
    return graph.compile()
