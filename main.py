import psycopg
from fastapi import FastAPI

from config import settings

app = FastAPI()


@app.get("/")
def root():
    return {"message": "guestbook"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/messages")
def list_messages():
    with psycopg.connect(settings.database_url) as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT id, author, text, created_at "
            "FROM messages ORDER BY created_at DESC"
        )
        rows = cur.fetchall()
    return [
        {"id": r[0], "author": r[1], "text": r[2], "created_at": r[3]}
        for r in rows
    ]


@app.post("/messages")
def add_message(payload: dict):
    with psycopg.connect(settings.database_url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO messages (author, text) VALUES (%s, %s) RETURNING id",
                (payload["author"], payload["text"]),
            )
            new_id = cur.fetchone()[0]
        conn.commit()
    return {"id": new_id}