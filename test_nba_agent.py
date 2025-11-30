from asyncio import sleep
import os
import pytest 
import logging
from nba_agent import get_scores
from monocle_test_tools import MonocleValidator
logging.basicConfig(level=logging.WARN)

agent_test_cases:list[dict] = [
    {
        "test_input": ["What happened in Clippers game on 22 Nov 2025"],
        "test_output": "Clippers won against Hornets with score 131-116 on 11/22/2025.",
        "comparer": "similarity",
        "test_spans": [
            {
            "span_type": "agentic.tool.invocation",
            "entities": [
                {"type": "tool", "name": "get_nba_past_scores"},
                {"type": "agent", "name": "Nba_scores_agent"}
                ]
            }
        ]
    },
]

# @pytest.mark.parametrize("test_case", agent_test_cases) #, ids = MonocleValidator.test_id_generator)
@MonocleValidator().monocle_testcase(agent_test_cases)
def test_run_workflows(test_case: dict):
    MonocleValidator().test_workflow(get_scores, test_case)

if __name__ == "__main__":
    pytest.main([__file__]) 