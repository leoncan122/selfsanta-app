from fastapi import FastAPI, WebSocket


class SocketRepository:
    def __init__(self):
        self.connections = {}
        
    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.connections[user_id] = websocket
        print(f"User {user_id} connected.")
    
    async def disconnect(self, user_id: str):
        if user_id in self.connections:
            websocket = self.connections[user_id]
            await websocket.close()
            del self.connections[user_id]
            print(f"User {user_id} disconnected.")
        else:
            print(f"User {user_id} not found in connections.")
    
    async def send_message(self, user_id: str, message: str):
        if user_id in self.connections:
            websocket = self.connections[user_id]
            await websocket.send_text(message)
            print(f"Message sent to {user_id}: {message}")
        else:
            print(f"User {user_id} not connected, cannot send message.")
            