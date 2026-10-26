from fastapi import FastAPI, Header, Request

app = FastAPI(title="CodeSage Auditor", version="1.0.0")

@app.get("/")
def health():
    return {"status": "ready", "agent": "CodeSage Autonomous Auditor"}

@app.post("/webhook/github")
async def github_webhook(request: Request, x_github_event: str = Header(None)):
    payload = await request.json()
    action = payload.get("action")
    return {"event": x_github_event, "action": action, "status": "analyzing_ast"}
