from fastapi import APIRouter

router = APIRouter(prefix="/v2", tags=["Landing Page"])


@router.get("/landing-page")
def landing_page_api():
    response = {
        "slug": "samsung-s26-ultra-hot-sale"
    }
    return response
