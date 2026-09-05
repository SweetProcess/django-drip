# django-drip development instructions

django-drip is a maintained dependency used by SweetProcess.

## General rules

- Preserve backwards compatibility unless explicitly asked otherwise.
- Do not change runtime behavior during tooling or packaging changes.
- Add regression tests before fixing behavioral bugs.
- Run the full test suite after production-code changes.
- Keep migrations compatible with existing django-drip installations.
- Do not regenerate or squash existing migrations without explicit approval.
- Do not introduce runtime dependencies without explaining why.
- Prefer Django public APIs over internal APIs.

## Supported environment

- Python: 3.12, 3.13, 3.14
- Django: 5.1, 5.2, 6.0, 6.1

## Scope

This repository is intentionally small. Prefer simple implementations
over adding new abstractions or frameworks.