from fastapi import FastAPI, WebSocket

app = FastAPI()

from app.publisher.api import publisher

# app.include_router(publisher.router, prefix="/messages")

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_json(data)