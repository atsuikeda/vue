from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_trivia():
    return {"fact": "test"}

@router.get("/random")
def get_random_trivia():
    return {"fact": "Another test fact"}