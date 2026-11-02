"""Standalone, deterministic tool-execution authorization starter.

This is *not* an A2A implementation or an LLM judge. Any A2A runtime should
call this trusted authorization boundary *before* executing a mock tool.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    actor: str
    original_task: str
    action: str
    data_classification: str
    destination: str | None = None
    delegation_chain: tuple[str, ...] = ("user", "agent_a", "agent_b")


ALLOWED_ACTIONS = frozenset({"ledger.read_internal", "summary.generate"})
ALLOWED_ACTORS = frozenset({"agent_b"})


def authorize(request: Request) -> tuple[bool, str]:
    """Authorize using trusted context, not assertions in an agent message."""
    if request.actor not in ALLOWED_ACTORS:
        return False, "actor_not_authorized"
    if request.original_task != "synthetic_ledger_summary":
        return False, "unrecognized_original_task"
    if request.delegation_chain != ("user", "agent_a", "agent_b"):
        return False, "invalid_delegation_chain"
    if request.action not in ALLOWED_ACTIONS:
        return False, "action_not_authorized"
    if request.destination is not None:
        return False, "external_destination_not_authorized"
    if request.data_classification not in {"synthetic_raw", "synthetic_aggregate"}:
        return False, "unknown_data_classification"
    if request.action == "summary.generate" and request.data_classification != "synthetic_aggregate":
        return False, "summary_must_be_aggregate"
    return True, "authorized"
