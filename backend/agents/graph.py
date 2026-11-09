"""
LangGraph Multi-Agent Orchestration Workflow.
Compiles a state graph with conditional branching between discovery, comparison,
evaluation, pricing intelligence, sentiment mining, and market trend nodes.
"""

from langgraph.graph import StateGraph, END
from backend.agents.state import AgentState
from backend.agents.nodes import (
    router_node,
    discovery_agent,
    comparison_agent,
    evaluation_agent,
    business_pricing_agent,
    business_sentiment_agent,
    business_trends_agent,
    synthesizer_node
)

def route_intent(state: AgentState) -> str:
    """
    Conditional router mapping state intent to corresponding agent node.
    """
    mode = state.get("mode", "shopping")
    intent = state.get("intent", "discovery")

    if mode == "business":
        if intent == "sentiment_intel":
            return "business_sentiment"
        elif intent == "market_trends":
            return "business_trends"
        else:
            return "business_pricing"
    else:
        if intent == "compare":
            return "comparison"
        elif intent == "evaluate":
            return "evaluation"
        else:
            return "discovery"


def create_agent_graph():
    """
    Constructs and compiles the multi-agent LangGraph workflow.
    """
    workflow = StateGraph(AgentState)

    # Register Nodes
    workflow.add_node("router", router_node)
    workflow.add_node("discovery", discovery_agent)
    workflow.add_node("comparison", comparison_agent)
    workflow.add_node("evaluation", evaluation_agent)
    workflow.add_node("business_pricing", business_pricing_agent)
    workflow.add_node("business_sentiment", business_sentiment_agent)
    workflow.add_node("business_trends", business_trends_agent)
    workflow.add_node("synthesizer", synthesizer_node)

    # Set Entry Point
    workflow.set_entry_point("router")

    # Conditional branching from router to specialized agents
    workflow.add_conditional_edges(
        "router",
        route_intent,
        {
            "discovery": "discovery",
            "comparison": "comparison",
            "evaluation": "evaluation",
            "business_pricing": "business_pricing",
            "business_sentiment": "business_sentiment",
            "business_trends": "business_trends"
        }
    )

    # All specialized agents flow into the SynthesizerNode
    workflow.add_edge("discovery", "synthesizer")
    workflow.add_edge("comparison", "synthesizer")
    workflow.add_edge("evaluation", "synthesizer")
    workflow.add_edge("business_pricing", "synthesizer")
    workflow.add_edge("business_sentiment", "synthesizer")
    workflow.add_edge("business_trends", "synthesizer")

    # Synthesizer completes the graph execution
    workflow.add_edge("synthesizer", END)

    app = workflow.compile()
    return app

# Singleton compiled LangGraph application
multi_agent_app = create_agent_graph()
