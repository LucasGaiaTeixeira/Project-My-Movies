from pydantic import BaseModel, Field
from schemas.movies import MovieRecommendation


class RecomendationRequest(BaseModel):
    textInput: str = Field(
        ...,
        max_length=500,
        min_length=10,
        description="description user preferences to find movies"
        )
    
class RecomendationResponse(BaseModel):
    sucess: bool = Field(..., description="If the recommendation ")
    data: MovieRecommendation = Field(..., description="Recommendation data")
    message: str = Field(..., description="Message information")
