# Notes — One Word, One Username, One Reward

- Bounty: https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae
- Prize: $5 total (1st $2 / 2nd $2 / 3rd $1). Free entry, no prerequisites.
- Opened: 24 Nov 2026 ~08:00 WIB. Entries close: 27 Nov 2026 06:50 WIB (26 Nov 23:50 UTC).
- Blind rounds: 6 rounds; R1 cutoff 24 Nov 18:48 WIB, R2 25 Nov 06:49 WIB,
  R3 25 Nov 18:49 WIB, R4 26 Nov 06:49 WIB, R5 26 Nov 18:49 WIB, final
  27 Nov 06:50 WIB. Results 19 Dec 2026.
- Harness: program/v1. Program writes `/output/entry.txt`; gate checks
  UTF-8 text, 1–30 characters, not only whitespace.
- Field at build time: 4 submissions (small table).
- Entry v1 username (12 chars):

  ```
  joni-gunawan
  ```

## Live score / rank

- (pending submit + round 1 — blind rounds, no live score until a round closes)

## Build log

- Built 24 Nov ~10:35 WIB after Joni's "Lanjutkan" (builder had been
  blocked before code was written). Kit downloaded fresh from
  https://make.fun/c/<slug>/kit; kit init anchor 279d2f9, drand round
  34229011.
- Genuine revision (thinking_revised): added `validate()` — fails loudly
  if the username is not exactly one word or outside the 1–30 char gate
  — + `test_gate_validation_rejects_bad_username`. Tests 6/6 pass.
- Entry commit 1507195c6da21126f1d2aa76c99138e9df4b4f3d (master),
  pushed to https://github.com/Ci3hu1/u-rusdyxbt-one-word-one-username-one-reward-1a191fae
  (verified via `git ls-remote`).
- Repo About verified: homepage = bounty page, topics ai-agents/bounties/makefun.
- Ready for Joni's 'Setuju' — bundle + check + submit after approval.
  No submit yet.
