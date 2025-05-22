from fastapi import APIRouter, HTTPException
from typing import Dict, Optional
import logging
from services.get_trivia import trivia_service

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get(
    "/random",
    response_model=Dict[str, str],
    summary="ランダムな豆知識を取得",
    description="ランダムな豆知識を取得し、指定された言語に翻訳して返します。"
)
async def get_random_trivia(target_lang: Optional[str] = "ja") -> Dict[str, str]:
    """
    ランダムな豆知識を取得し、指定された言語に翻訳して返す
    """
    try:
        logger.info(f"Received request for random trivia (target_lang: {target_lang})")
        trivia = await trivia_service.get_random_trivia(target_lang)
        logger.info("Successfully processed trivia request")
        return trivia
    except HTTPException as e:
        logger.error(f"HTTP Exception: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in router: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process trivia: {str(e)}"
        )