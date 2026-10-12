from agno.models.google import Gemini
from agno.agent import Agent
from agno.tools.websearch import WebSearchTools
from agno.models.groq import Groq

from agents.prompts.movie_search import instructions
from agents.prompts.movie_search import description

from schemas.movies import MovieRecommendation

from agents.tools.ombd_api import search_filmes
from config.config_env import Enviroments


movie_recommendation_agent = Agent(
    name="my-movies",
    description=description,
    instructions=instructions,
    model=Gemini(
        id=Enviroments.model_ai_validation_gemini(),
        api_key=Enviroments.api_key_gemini_validation(),
    ),
    tools=[WebSearchTools(backend="duckduckgo"), search_filmes],
    markdown=True,
    add_datetime_to_context=True,
    output_schema=MovieRecommendation,#aqui ele ja desserializa o objeto que vem em json pelo modelo e transforma em objetos python, entao nao precisa de outro desserializador
    debug_mode=True,
    debug_level=1 # e o level de que mostra oque a Ia esta fazendo
)


async def recommendations(request: str):
    result = await movie_recommendation_agent.arun(request, stream=False)#metodo para rodar o codigo do agente de forma assincrona

    # if(result.content and result):
    #     #data: MovieRecommendation = result.content.json() #ele desserializa para objetos python esse .json() que vai ser do tipo MovieRecomendation que criei para ser como dataTrasnferObject, servir como o modelo da requisição e ter os objetos python
    #     data_json_output = result.content.model_dump_json(indent=2) #aqui ele trasforma string de texto ou objetos python em json novamente
    #     print(data_json_output)

    return result.content
    