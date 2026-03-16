# Ticket API

API REST de gestion de tickets développée avec FastAPI.

# Fonctionnalités
- Créer un ticket
- Lister les tickets
- Récupérer un ticket par ID
- Modifier un ticket
- Fermer un ticket

# Stack
- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite (in-memory)
- Pydantic
- Pytest
- Ruff (linting)
- Docker
- Makefile

# Installation locale

## 1. Cloner le projet
- git clone git@github.com:Tareksekrafii/ticket-api.git
- cd ticket-api

## 2. Créer un environnement virtuel
- python3 -m venv .venv
- source .venv/bin/activate

## 3. Installer les dépendances
pip install -r requirements.txt


# Lancer l'API
uvicorn app.main:app --reload

- L'API sera accessible sur : http://127.0.0.1:8000
- Documentation Swagger : http://127.0.0.1:8000/docs

# Tests :
- Lancer les tests : pytest
- Coverage : pytest --cov=app --cov-report=term-missing

# Linting
Lancer Ruff :ruff check .

# Makefile
Commandes disponibles :
- make install
- make run
- make test
- make coverage
- make lint

# Docker
- Construire l'image : docker build -t ticket-api .
- Lancer le container : docker run -p 8000:8000 ticket-api
