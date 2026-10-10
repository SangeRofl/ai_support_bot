from fastapi import FastAPI
from api.routers.faq import router as faq_router

app = FastAPI(title='AI Support Bot API')


app.include_router(
    faq_router,
    prefix="/api/v1",
)



@app.get("/health")
async def health_check():
    return {"status": "ok"}
