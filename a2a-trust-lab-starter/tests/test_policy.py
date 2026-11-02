import unittest

from policy import Request, authorize


class PolicyTests(unittest.TestCase):
    def test_summary_allowed(self):
        request = Request("agent_b", "synthetic_ledger_summary", "summary.generate", "synthetic_aggregate")
        self.assertEqual(authorize(request), (True, "authorized"))

    def test_internal_read_allowed(self):
        request = Request("agent_b", "synthetic_ledger_summary", "ledger.read_internal", "synthetic_raw")
        self.assertTrue(authorize(request)[0])

    def test_raw_export_denied_even_with_forced_task_goal(self):
        request = Request("agent_b", "synthetic_ledger_summary", "record.export_raw", "synthetic_raw", "reviewer@example.test")
        self.assertEqual(authorize(request), (False, "action_not_authorized"))

    def test_improper_delegation_denied(self):
        request = Request("agent_b", "synthetic_ledger_summary", "summary.generate", "synthetic_aggregate", delegation_chain=("agent_a", "agent_b"))
        self.assertEqual(authorize(request), (False, "invalid_delegation_chain"))

    def test_unknown_actor_denied(self):
        request = Request("agent_a", "synthetic_ledger_summary", "summary.generate", "synthetic_aggregate")
        self.assertEqual(authorize(request), (False, "actor_not_authorized"))

    def test_external_destination_denied_even_for_aggregate(self):
        request = Request("agent_b", "synthetic_ledger_summary", "summary.generate", "synthetic_aggregate", "reviewer@example.test")
        self.assertEqual(authorize(request), (False, "external_destination_not_authorized"))


if __name__ == "__main__":
    unittest.main()
