from fastapi import FastAPI
import os
import json

app = FastAPI()


@app.get("/")
async def root():

    files = os.listdir('fhir_resources')

    patients = []
    for filename in files:
        with open(f"fhir_resources/{filename}") as file:
            patients.append(json.load(file))

    return patients
