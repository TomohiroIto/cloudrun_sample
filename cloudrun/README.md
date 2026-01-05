uv python list
uv python install 3.14

uv venv -p 3.14 .venv

.venv\Scripts\activate.bat
uv init --name cloudrun


uv pip compile pyproject.toml > requirements.txt


uv add --dev pytest
#uv add fastapi "uvicorn[standard]"
pip install uvicorn

uv add jinja2 pydantic

uvicorn app1.main:app --reload --host 0.0.0.0 --port 8081
