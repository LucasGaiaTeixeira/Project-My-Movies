from agents.core.movie_search_agent import recommendations
from schemas.api_movie import RecomendationRequest, RecomendationResponse
from fastapi import HTTPException

async def service_api_movie(resquest: RecomendationRequest):
    try:
        recommendations_request = await recommendations(resquest.textInput)

        if(not recommendations_request):
            raise HTTPException (
                status_code=500,
                detail="create recommended movie error"
            )

        return RecomendationResponse(
            sucess=True,
            data= recommendations_request,
            message="Recommendations create sucess!"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"error to process Recomendation, {e}", 
        )
        