from fastapi.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(__name__ + ":app", port=5000, log_level="info")
