from fastapi import APIRouter
from service.agent_service import service_api_movie
from schemas.api_movie import RecomendationResponse, RecomendationRequest

agent_routes = APIRouter(prefix="/talk")



@agent_routes.post(
    "/new_recommendation",
    response_model=RecomendationResponse,
    description="Create personalized recommendations to movie for user ",
    summary="To take Recommendations movies",
    tags=["Recomendation"]
    )
async def talk_ai_recommendation(request: RecomendationRequest) -> RecomendationResponse:
    return await service_api_movie(request)


@agent_routes.get(
        "/health",
        description="only test for api is online",
        tags=["System"]
        )
def helth_api():
    """test if api is online"""
    return {
        "test": "ok",
    }