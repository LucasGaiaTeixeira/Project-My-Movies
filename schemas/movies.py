from pydantic import BaseModel, Field

class Cast(BaseModel):
    """informations about film's cast"""
    name: str = Field(..., description="name of the actor/actress")#esse ... indica ao pydantic que essa variavel, precisa receber um valor, senão ela retorna um erro
    personagem: None | str = Field(None, description="the actor's character name")

class Movie(BaseModel):
    """Model structured for movie data"""
    title: str = Field(..., description="title movie")
    release_year: int = Field(..., description="release year")
    director: str = Field(..., description="principal director")
    genres: list[str] = Field(..., description="genres and subgenres")
    imdb_rating: float = Field(..., description="Classification IMDB (focus em 7.5+)")
    duration_minutes: int = Field(..., description="Duration in minutes")
    primary_language: str = Field(..., description="principal language")
    synopsis: str = Field(..., description="brief and engaging synopsis")
    age_rating: str = Field(..., description="age rating(ex: PG, PG-13, 16, 18)")
    content_warnings: list[str] | None = Field(None, description="content warnings")
    cast:list[Cast] = Field(default_factory=list, description="remarkable cast") # esse default_factory, quer dizer que se a api não enviar nada, ele cria uma lista vazia para esse variavel
    poster_url: str | None = Field(None, description="poster URL")
    streaming_platforms: list[str] | None = Field(None, description="Streamming platform")
    recommendation_reason: str = Field(..., description="brief explanation and recomendation")

class MovieRecommendation(BaseModel):
    """Structured response with multiples recomendations"""
    movie: list[Movie] = Field(..., description="movie recomendations list(minimo:5)")
    total_recommendations: int | None = Field(None, )