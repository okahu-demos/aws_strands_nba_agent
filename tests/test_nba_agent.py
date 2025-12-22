
import pytest 
import logging
from nba_agent import get_scores
from monocle_test_tools import TraceAssertion

@pytest.mark.asyncio
async def test_tool_invocation(monocle_trace_asserter:TraceAssertion):
    """Test that the correct tool is invoked and returns expected output."""
    get_scores("What happened in Clippers game on 22 Nov 2025")

    monocle_trace_asserter.called_tool("get_nba_past_scores")

    monocle_trace_asserter.called_agent("Nba Score Agent")

    monocle_trace_asserter.called_tool("get_nba_past_scores").contains_input("Clippers").contains_output("Hornets")

    monocle_trace_asserter.called_agent("Nba Score Agent").has_input("What happened in Clippers game on 22 Nov 2025").contains_output("Hornets").contains_output("131-116")

if __name__ == "__main__":
    pytest.main([__file__]) 
