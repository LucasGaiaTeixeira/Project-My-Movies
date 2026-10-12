import aiohttp

from config.config_env import Enviroments
 
async def search_filmes(title: str) -> dict[str, list[str]] | str :
    """
        this tool take the title from movie and find in Api OMBD to movie in database him

        args:
            title(string): movie titile
        
        returns:
            2 things:
                1: a Dictionary from movie content information of OMBD data movie
                or
                2: errors in string
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                "http://www.omdbapi.com/",
                params={
                    "api_key": Enviroments.api_key_ombd_validation(), #api key
                    "t": title, # titulo do filme que é passado na função
                    "type": "movie", # se vai ser filme, serie ou episodeo
                    "plot": "full", #a sinopse do filme/serie/episodeo que foi escolhido em type
                    "v": "1" # versão da api
                },        
                timeout=aiohttp.ClientTimeout(total=10) # essa linha serve para que se depois de 10 segundos não chegar uma requisiçao ele solte um error
            ) as response:
                if response.status != 200:
                    return f"error retrieiving the movie {response.status}"

                data = await response.json() # pega os dados em em json e disserializa em objetos python

                if(response.get("Response") == "False"): #na api a chave precisa estar True, porque se não os dados vao estar incompletos
                    return f"incomplete data movies from {title}"

                return data
                

        except aiohttp.ClientError as e:
            raise (f"find movie error in {title}", e)