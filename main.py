from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import uvicorn
from api.agent_routes import agent_routes

app = FastAPI(
    title="My_Filmes",#titulo do app
    description="you are a software to Recomendation movies", #descrição do app
    docs_url="/docs",# aonde se enconta os documentos no swagger em /docs
    redoc_url="/redoc", # encontra os documentos no formato redoc
    version="1.0"#versão da aplicação
)


app.include_router(agent_routes)

#configura cors para acesso externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #origen de aonde vai ser transmitido o app, pode ser colocado em produção também
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)


if(__name__ == "__main__"):
    uvicorn.run(
        "main:app",
        port=8000,
        host="0.0.0.0",
        log_level="info",
        access_log=True,
        reload=True
    )