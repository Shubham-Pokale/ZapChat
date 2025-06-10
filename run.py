import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="http://127.0.0.1/",
        port=8000,
        reload=True,
        debug=True
    ) 