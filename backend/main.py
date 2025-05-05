# backend/main.py

import asyncio
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
import asyncio
from backend.services.strategy_service import StrategyService, run_live_trader
from backend.services.smartapi_service import SmartAPIService
from backend.services.persistence import init_db, get_db, sync_trades, get_running_pnl, get_closed_positions

app = FastAPI()

# 1) serve your built SPA
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    return FileResponse("frontend/index.html")
    
 

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # 1) log into SmartAPI
    SmartAPIService.login()

    # 2) load & instantiate all strategies
    StrategyService.load_strategies()

    # 3) kick off the live‐trader loop in the background
    asyncio.create_task(run_live_trader())


@app.post("/api/sync")
def api_sync(db=Depends(get_db)):
    try:
        sync_trades(db)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/api/dashboard")
def api_dashboard(db=Depends(get_db)):
    running = get_running_pnl(db)
    closed = get_closed_positions(db)
    return {"running_pnl": running, "closed_positions": closed}
