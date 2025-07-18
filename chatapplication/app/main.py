from fastapi import FastAPI, Depends
from app.auth import router as auth_router
from app.dependencies import require_role

app = FastAPI()

app.include_router(auth_router)

@app.get("/admin-only")
def admin_route(user=Depends(require_role("admin"))):
    return {"message": f"Hello Admin {user.username}!"}

@app.get("/user-only")
def user_route(user=Depends(require_role("user"))):
    return {"message": f"Hello User {user.username}!"}
