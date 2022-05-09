from typing import List

from fastapi import Cookie, Depends, FastAPI, Query, WebSocket, status, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from pixel_map import PixelMap


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


class Server():

    def __init__(self):
        self.app = FastAPI()
        self.manager = ConnectionManager()
        self.pixel_map = PixelMap()

        @self.app.get("/")
        async def get():
            return ""

        @self.app.get("/status")
        async def get():
            return self.pixel_map.return_matrix()

        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await self.manager.connect(websocket)
            await self.manager.send_personal_message("TEST", websocket)
            try:
                while True:
                    data = await websocket.receive_text()
                    self.pixel_map.modify_pixel(data)
                    await self.manager.broadcast(data)
            except WebSocketDisconnect:
                self.manager.disconnect(websocket)
