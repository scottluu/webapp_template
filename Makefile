venv:
	python -m venv .venv
	./.venv/Scripts/pip.exe install poetry
	./.venv/Scripts/poetry.exe install
