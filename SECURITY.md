# Security Policy

## Supported Use

This repository is a template and starter project. Security-sensitive changes should be treated seriously, especially in these areas:

- token and secret handling
- permission checks
- moderation actions
- file exports and transcripts
- voice and external media processing
- user-generated content embedded into messages

## Reporting a Vulnerability

Do not open a public issue for a live security problem involving secrets, abuse paths, or moderation bypasses.

Instead, report privately to the repository owner with:

- affected file or feature
- reproduction steps
- expected impact
- suggested fix, if known

## Hardening Recommendations

- keep bot tokens only in `.env`
- give the bot the minimum Discord permissions it needs
- avoid enabling privileged intents unless required
- validate and clamp user inputs
- avoid mass actions without confirmation prompts
- keep FFmpeg and Python dependencies updated
- audit owner-only and admin-only commands carefully