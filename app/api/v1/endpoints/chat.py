from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, Depends
from app.core.ws_manager import manager
from app.core.security import get_websocket_user, Session
from app.db.base import get_db

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...),
    db: Session = Depends(get_db)
):
    user = await get_websocket_user(websocket, token, db)
    
    await manager.connect(websocket, user)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(
                message=data,
                sender_id=user.id
            )
    except WebSocketDisconnect:
        manager.disconnect(user.id)