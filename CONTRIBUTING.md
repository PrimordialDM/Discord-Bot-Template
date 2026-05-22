# Contributing

Thanks for contributing to PrimordialDM's Discord Bot Master Reference.

## Scope

This repository contains two things:

- a large master reference file for copy-paste adoption
- a clean modular starter for developers who want a sane public repo layout

Contributions should improve one of these without making the repository harder to understand.

## Contribution Rules

- Keep changes focused.
- Preserve author credit to PrimordialDM.
- Prefer small, composable templates over tightly coupled code.
- Avoid adding hidden external service requirements.
- Document any new environment variable in `.env.example` and `README.md`.
- If you add a dependency, update `requirements.txt` and explain why in the PR.

## Development Guidelines

- Target Python 3.10+
- Use `discord.py` idioms
- Keep slash commands typed and documented
- Prefer reusable helpers in `utils/` and `views/`
- Keep example data safe to commit; never commit secrets

## Before Opening a PR

1. Run a syntax check on the changed Python files.
2. Confirm `.env.example` still matches the code.
3. Update README sections affected by your change.
4. Keep runtime files out of git.

## Pull Request Notes

Include:

- what changed
- why it changed
- whether it affects the modular starter, the master reference, or both
- any new env vars, commands, or dependencies
