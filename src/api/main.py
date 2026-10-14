from fastapi import FastAPI
from src.api.routers.faq import router as faq_router

app = FastAPI(title='AI Support Bot API')


app.include_router(
    faq_router,
    prefix="/api",
)



@app.get("/health")
async def health_check():
    return {"status": "ok"}

