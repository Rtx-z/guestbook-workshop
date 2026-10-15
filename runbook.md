# guestbook-workshop
Сервис гостевой книги на FastAPI. Собирается в Docker-образ,
публикуется в GHCR по релизным тегам `vX.Y.Z`.
## Стек
- Python 3.12
- FastAPI + Uvicorn
- PostgreSQL
- uv (управление зависимостями)
- Ruff (линтер), pytest (тесты)
- Docker, GitHub Actions, GHCR
## Требования

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker (для сборки образа)
- PostgreSQL (локально или в контейнере)
## Быстрый старт

```bash
git clone https://github.com/Rtx-z/guestbook-workshop.git
cd guestbook-workshop
uv sync
cp .env.example .env       # и заполнить POSTGRES_*
uv run uvicorn main:app --reload

