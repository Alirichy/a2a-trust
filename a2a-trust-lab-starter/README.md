# A2A Trust Boundary Lab

**Status:** Research design and local policy-test starter, NOT a completed multi-agent experiment.

The aim is to determine whether one agent can convince another to execute an operation beyond the human user's originally delegated authority. It is deliberately limited to **synthetic data, mock actions, and local processes**.

## Research question

> When Agent A delegates a legitimate task to Agent B, can a malicious or overzealous message cause Agent B to perform an unauthorized action? Does deterministic tool-level enforcement prevent execution?

**Distinguish three outcomes:**
1. **Attempt:** An LLM/agent requested a prohibited action.
2. **Execution:** The mock tool actually performed the prohibited action. This is an enforcement failure.
3. **Task success:** The legitimate user request was completed.

This starter provides a synthetic dataset, a policy-enforcement function, unit tests, and a complete Codex implementation brief. It **does not yet run live agents or the A2A Python SDK**. Ask Codex to implement the runtime described in `CODEX_TASK.md`.

## Getting started

From the directory:

```bash
python -m unittest discover -s tests -v
```

When you're back at a computer, open the folder and run `codex`. Paste the contents of `CODEX_TASK.md` or ask Codex to read and implement it.

## Guardrails

- Never connect this experiment to company systems, customer data, or actual sending/transfer tools.
- All mock emails are only appended to local in-memory or on-disk event logs.
- A2A servers (when added) bind to `127.0.0.1` only.
- A result from an intentionally insecure demo implementation is **not** evidence that the A2A protocol itself has a vulnerability.
- Keep the difference between prompt-injection susceptibility and missing authorization checks explicit.

## Sources

- Official A2A specification: https://a2a-protocol.org/dev/specification/
- A2A Python tutorial: https://github.com/a2aproject/A2A/blob/main/docs/tutorials/python/1-introduction.md
- Official A2A examples: https://github.com/a2aproject/a2a-samples
