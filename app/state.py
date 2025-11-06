from typing import TypedDict, Optional

class AgentState(TypedDict):
    input: str
    result: Optional[str]
