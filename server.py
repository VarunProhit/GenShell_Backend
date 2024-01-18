from typing import Union
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from GenAI import GenerativeAI
app = FastAPI()


@app.post("/generate")
async def genCommand(body = Body(...)):
    body=jsonable_encoder(body)
    print(body,type(body))
    query = body["input"]
    generativeAI = GenerativeAI()
    # re = str(line)
    command = generativeAI.generate_response(query)
    print(command)
    return command
