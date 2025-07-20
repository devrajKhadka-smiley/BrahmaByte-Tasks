from fastapi import FastAPI
from app.auth import router as auth_router
from app.admin import router as admin_router
from app.websocket import router as ws_router

app = FastAPI(
    title="FastAPI Chat App",
    description="A chat system with WebSocket, JWT auth, and admin control.",
    version="1.0.0"
)

# Include routers only once
app.include_router(auth_router)
app.include_router(ws_router)
app.include_router(admin_router)


# @app.get("/admin-only")
# def admin_route(user=Depends(require_role("admin"))):
#     return {"message": f"Hello Admin {user.username}!"}

# @app.get("/user-only")
# def user_route(user=Depends(require_role("user"))):
#     return {"message": f"Hello User {user.username}!"}

