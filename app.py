from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE = 'voting_system.db'

# Ensure the database and tables are created
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE users (
        user_id TEXT PRIMARY KEY,
        public_key TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE elections (
        election_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        candidates TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE votes (
        vote_id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        election_id TEXT NOT NULL,
        candidate TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(election_id) REFERENCES elections(election_id)
    )
    ''')
    # Seed data
    cursor.execute("INSERT INTO users (user_id, public_key) VALUES ('user1', 'key1')")
    cursor.execute("INSERT INTO elections (election_id, name, candidates) VALUES ('election1', 'Presidential Election', 'Candidate A,Candidate B')")
    conn.commit()
    conn.close()

# Models
class User(BaseModel):
    user_id: str
    public_key: str

class Election(BaseModel):
    election_id: str
    name: str
    candidates: list

class Vote(BaseModel):
    vote_id: str
    user_id: str
    election_id: str
    candidate: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/elections", response_class=HTMLResponse)
async def manage_elections(request: Request):
    return templates.TemplateResponse("elections.html", {"request": request})

@app.get("/vote", response_class=HTMLResponse)
async def cast_vote(request: Request):
    return templates.TemplateResponse("vote.html", {"request": request})

@app.get("/results", response_class=HTMLResponse)
async def election_results(request: Request):
    return templates.TemplateResponse("results.html", {"request": request})

@app.post("/api/register")
async def register_user(user: User):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (user_id, public_key) VALUES (?, ?)", (user.user_id, user.public_key))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="User already registered")
    finally:
        conn.close()
    return {"message": "User registered successfully"}

@app.post("/api/create-election")
async def create_election(election: Election):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO elections (election_id, name, candidates) VALUES (?, ?, ?)", (election.election_id, election.name, ','.join(election.candidates)))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Election already exists")
    finally:
        conn.close()
    return {"message": "Election created successfully"}

@app.get("/api/elections")
async def get_elections():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT election_id, name, candidates FROM elections")
    elections = cursor.fetchall()
    conn.close()
    return [{"election_id": e[0], "name": e[1], "candidates": e[2].split(',')} for e in elections]

@app.post("/api/vote")
async def cast_vote(vote: Vote):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (vote.user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    cursor.execute("SELECT * FROM elections WHERE election_id = ?", (vote.election_id,))
    election = cursor.fetchone()
    if not election:
        raise HTTPException(status_code=404, detail="Election not found")
    cursor.execute("INSERT INTO votes (vote_id, user_id, election_id, candidate) VALUES (?, ?, ?, ?)", (vote.vote_id, vote.user_id, vote.election_id, vote.candidate))
    conn.commit()
    conn.close()
    return {"message": "Vote cast successfully"}

@app.get("/api/results")
async def get_results(election_id: str):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT candidate, COUNT(candidate) FROM votes WHERE election_id = ? GROUP BY candidate", (election_id,))
    results = cursor.fetchall()
    conn.close()
    return {"election_id": election_id, "results": {r[0]: r[1] for r in results}}
