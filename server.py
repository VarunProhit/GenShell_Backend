from typing import Union
from fastapi import FastAPI, Request, Response, Body, status
from fastapi.encoders import jsonable_encoder
from GenAI import GenerativeAI
from utils import HTTP

app = FastAPI()


@app.post("/generate")
async def genCommand(request: Request, response: Response, body = Body(...)):
    http = HTTP(response)
    body = jsonable_encoder(body)
    print(body, type(body))
    if "input" not in body:
        return http.response(status.HTTP_400_BAD_REQUEST, "input is required")
    query = body["input"]
    generativeAI = GenerativeAI()
    # re = str(line)
    command = generativeAI.generate_response(query)
    print(command)
    return command
