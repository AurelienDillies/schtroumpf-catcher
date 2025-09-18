from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .routes import items
import os

app = FastAPI()

# Autoriser ton front à accéder à l’API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en prod : limiter au domaine du front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(items.router)

# 📂 Servir les fichiers statiques (CSS, JS, images)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# 📄 Routes pour tes pages HTML
@app.get("/")
def serve_index():
    return FileResponse(os.path.join("frontend", "html/index.html"))

@app.get("/carte")
def serve_carte():
    return FileResponse(os.path.join("frontend", "html/carte.html"))

@app.get("/ajout")
def serve_ajouter():
    return FileResponse(os.path.join("frontend", "html/ajout.html"))

@app.get("/contact")
def serve_contact():
    return FileResponse(os.path.join("frontend", "html/contact.html"))

@app.get("/connexion")
def serve_connexion():
    return FileResponse(os.path.join("frontend", "html/connexion.html"))