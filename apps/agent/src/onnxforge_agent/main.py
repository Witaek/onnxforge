from fastapi import FastAPI

app = FastAPI(title = "ONNXForge Agent")

@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "onnxforge-agent"
    }