from fastapi import APIRouter


router = APIRouter(
    prefix="/faq",
    tags=["faq"],
)

@router.get("/")
async def get_faq():
    return [
        {
            'id': 1,
            'question': 'Как вернуть товар?',
            "answer": "Для возврата товара обратитесь в поддержку.",
        }
    ]

