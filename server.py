from fastapi import FastAPI, Response, Body, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from GenAI import GenerativeAI
from utils import HTTP

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def gen_command(response: Response, body=Body(...)):
    http = HTTP(response)
    try:
        req_body = jsonable_encoder(body)
        query = req_body.get("input", None)
        if not query:
            return http.response(status.HTTP_400_BAD_REQUEST, "input is required")
        generative_ai = GenerativeAI()
        command = generative_ai.generate_response(query)
        return http.response(status.HTTP_200_OK, command)
    except Exception as e:
        return http.response(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
