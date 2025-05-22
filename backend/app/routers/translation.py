from fastapi import APIRouter, HTTPException
from schemas.translation import TranslationRequest, TranslationResponse
from services.translation import translation_service

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        translated_text = await translation_service.translate_text(
            request.text,
            request.source_lang,
            request.target_lang
        )
        return TranslationResponse(
            translated_text=translated_text,
            source_lang=request.source_lang,
            target_lang=request.target_lang
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed: {str(e)}"
        )

# 利用可能な言語のリストを取得するエンドポイント
@router.get("/languages")
async def get_languages():
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "ja", "name": "Japanese"},
            {"code": "zh", "name": "Chinese"},
            {"code": "ko", "name": "Korean"},
            {"code": "es", "name": "Spanish"},
            {"code": "fr", "name": "French"},
            {"code": "de", "name": "German"},
            {"code": "it", "name": "Italian"},
            {"code": "ru", "name": "Russian"}
        ]
    }
