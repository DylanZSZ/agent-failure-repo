# Starting environment

No external services, credentials, or GPU required. Pure local Python
(3.9+ for `list[str]`-style generic hints; rewrite the type hints for older
interpreters if needed).

Setup (idempotent, refuses to overwrite): the judge creates a fresh temp
directory per run and populates it with N fake, empty `step-%04d.parquet`
files (N chosen larger than any requested range, to simulate a shared
directory already populated by an earlier, unrelated full-range job — the
precondition that made the real incident latent). No real rollout data,
cluster paths, or credentials are used anywhere in this package.

Deterministic setup: see `task/repro.py`'s `make_fake_shards` for the exact
fixture-creation logic reused by the checks.
