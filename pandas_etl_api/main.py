from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pandas_etl_api.entities import AllActionsState
from pandas_etl_api.entities import Workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/api/actions")
async def get_actions() -> AllActionsState:
    return AllActionsState()


@app.post("/api/start", status_code=201)
async def start_etl(data: Workflow) -> dict:
    print(data)
    return {"message": "ETL started"}
