# Reviewer-owned checks

Implement a check independent of the evaluated agent's self-report. Keep it
outside the agent's workspace. Report setup validity, task correctness, and
the intended failure separately. Treat evaluated code as untrusted when a
judge imports or runs it. Metadata validation does not execute these files.

Before model execution, verify that each query and required field follows the
public contract at that stage, including roots, legal repeated operations, and
the first stage requiring each capability. Run a continuous correct path, a
different lawful implementation, and a lawful prefix implementation without
future capabilities through every stage of the actual checker. An early complete
reference implementation can conceal a query for an unpublished operation.
Evaluate candidate
code in a disposable copy; compare live files before and after even for queries.
Version later checker fixes without changing the original run record.
