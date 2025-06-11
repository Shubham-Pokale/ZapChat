from typing import Dict
from fastapi import WebSocket
from app.db.models import User

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        del self.active_connections[client_id]

    async def send_personal_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

    async def broadcast(self, message: str, sender_id: str = None):
        for client_id, connection in self.active_connections.items():
            if client_id != sender_id:
                await connection.send_text(message)

    async def broadcast_user_list(self):
        user_list = list(self.active_connections.keys())
        for connection in self.active_connections.values():
            await connection.send_json(
                {
                    "type": "user_list",
                    "users": user_list
                }
            )

manager = ConnectionManager()