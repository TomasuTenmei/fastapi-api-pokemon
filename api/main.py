from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.mongodb = app.mongodb_client["DB_NAME"]
    print("Connecté à la base de données !")
    
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Déconnecté de la base de données !")
