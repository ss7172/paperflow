from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import sqlite3

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/papers")
def get_papers():
    # conn = sqlite3.connect('papers.db')
    # cur = conn.cursor()
    # cur.row_factory = sqlite3.Row
    # cur.execute("SELECT * FROM papers")
    # rows = cur.fetchall()
    # conn.close()
    # return {"papers": [dict(row) for row in rows]}
    return FileResponse("static/index.html")
