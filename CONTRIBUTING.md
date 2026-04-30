# Contributing to Turing Wire

Thank you for your interest. A few notes before you open an issue or PR:

## This is a personal project

Pull requests are welcome but may not be reviewed quickly or merged. If you have a significant feature in mind, please open an issue first to discuss whether it fits the project's direction.

## What's welcome

- **Bug reports** — broken pipeline steps, incorrect company tagging, build failures.
- **Source suggestions** — missing AI lab blogs, research venues, or news outlets worth adding to `feeds/news_sources.yml` or `feeds/research_sources.yml`. Open an issue with the RSS/Atom URL and a brief rationale.
- **Company alias corrections** — open a PR editing `feeds/company_aliases.yml` if a company name is being missed or mis-tagged.
- **Typos and docs** — always welcome.

## What's out of scope

- Changing the core architecture (branch model, Jekyll, OpenAI, Finnhub).
- Adding features listed in "Out of scope for v1" in the design spec (user accounts, email newsletter, live streaming, mobile app).
- Scrapers for sites that prohibit automated access in their ToS.

## Code style

- Python: PEP 8, type hints on public functions, no unused imports.
- No new dependencies without a clear justification in the PR description.
- All secrets via environment variables — never hardcoded.

## Opening an issue

Please include:
1. What you expected to happen.
2. What actually happened (paste the relevant portion of the workflow log).
3. The date/time of the failed run so the maintainer can check the workflow artifact.
