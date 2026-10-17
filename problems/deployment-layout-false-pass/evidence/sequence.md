# Sanitized historical evidence account

This proposed derivative still needs owner review. Source A is one Codex reviewer session; source B is its coordinator. Their private original file paths and hashes are in the collection's private findings record. Line numbers below are original JSONL line numbers, not step counts. Event/response mirrors are counted once. Hidden reasoning was excluded from extraction and review.

Unless marked as a quotation, descriptions are investigator paraphrases. Project names, account names, cluster identifiers, exact release identifiers, hashes, job IDs and private paths are omitted. No historical command was rerun.

| UTC time on 2026-09-04 | Source anchor | Observation |
|---|---|---|
| 07:15:57.720 | A:3698 | The reviewer's tool result shows 25 local tests passed and manifest checks remained intact. |
| 07:16:07.461 | A:3703 | Tool output declares the deployed stage under the configured root, then `stages/<stage-id>`. |
| 07:16:11.468 | A:3708 | Tool output shows the guard requiring the stage basename to be `stage` and its parent basename to equal the release ID. That condition cannot accept `stages/<stage-id>`. |
| 07:18:47.240 | B:91800 | Actual remote read-only check exits 2. Short quoted error, with release identifier omitted: “launcher is not in its canonical stage path”. |
| 07:18:49.054 | A:3785 | Nine additional data-contract tests pass; manifest hashes remain unchanged. |
| 07:19:06.797 | A:3795 | Reviewer final report quotes: “PASS — no blocker found.” It lists the 25 plus nine passing tests. |
| 07:19:35.690 | A:3805 | Reviewer acknowledges that it missed the difference between local `<id>/stage` and deployed `stages/<id>` layouts. This corroborates the tool evidence; it is not the sole basis for the finding. |
| 07:21:10.480 | B:91875 | Coordinator identifies the local-only guard, preserves the failed immutable bytes and describes a replacement accepting both canonical layouts. |
| 07:34:51.944 | B:92217 | Replacement path smoke returns exit 0 and reports the expected resolved path. Output confirms no submission manifest or claim exists. |
| 07:36:48.092 | B:92241 | Full replacement remote check returns `check_pass`. |
| 07:36:57.476 | B:92246 | Follow-up check confirms no output, job or lock was created by the dry check. |

The failed remote check happened about 19.6 seconds before this reviewer's PASS, in a separate concurrent coordinator session. Its earlier result was not shown to have reached the reviewer before that PASS. The coordinator already had another reviewer's approval before staging, so causation from this reviewer to the deployment attempt is not claimed.

The path constant and incompatible guard were both visible to the reviewer before its final decision. This supports a missed contract check. A configured 258,400-token context window and a long inherited transcript do not establish that context length caused the miss. The source includes replayed ancestor records; the measured audit is approximately three and a half minutes.

Recovery is part of the record. The final deployed replacement passed the relevant checks. The source reviewer was interrupted later; its own session does not contain completion of the repair. Recovery evidence comes from B.

The exact delegated audit prompt was not recovered by the visible-history reader. The parent delegation payload is opaque, and the incoming agent-message record is outside the supported projection. Audit scope is therefore based on visible reviewer commentary, the code it inspected, surrounding coordinator activity and its later acknowledgement. Full instruction wording is unavailable; no opaque payload was decoded.
