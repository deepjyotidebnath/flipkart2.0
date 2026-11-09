"""
State schema for the Flipkart Intelligence Multi-Agent System.
"""

from typing import List, Dict, Any, Optional, TypedDict, Annotated
import operator

class AgentState(TypedDict):
    # User input and conversation
    messages: Annotated[List[Dict[str, str]], operator.add]
    user_query: str
    session_id: str
    mode: str  # "shopping" or "business"

    # Routing and classification
    intent: str  # "discovery", "compare", "evaluate", "pricing_intel", "sentiment_intel", "market_trends", "general"
    entities: Dict[str, Any]  # extracted budget, brand, category, target product names

    # Intermediate agent findings
    retrieved_products: List[Dict[str, Any]]
    retrieved_reviews: List[Dict[str, Any]]
    comparison_data: Optional[Dict[str, Any]]
    analytics_data: Optional[Dict[str, Any]]

    # Agent reasoning trail for full transparency in UI
    agent_trace: Annotated[List[Dict[str, Any]], operator.add]

    # Final outputs
    final_response: str
    recommended_products: List[Dict[str, Any]]
    quick_suggestions: List[str]
