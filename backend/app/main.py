# FastAPI is the web framework we use to build our API (like Express for Node, but for Python)
from fastapi import FastAPI

# CORSMiddleware lets our frontend (running on a different port) talk to this backend.
# Without this, the browser blocks requests between different origins (e.g., localhost:3000 -> localhost:8000).
# "CORS" stands for Cross-Origin Resource Sharing.
from fastapi.middleware.cors import CORSMiddleware

# Import the chat router from our routes folder.
# A "router" is a group of related endpoints. We define /chat in its own file to keep code organized.
# "as chat_router" just gives it a shorter name to use here.
from app.routes.chat import router as chat_router

# Create the FastAPI application instance. This is the main object that handles all incoming requests.
# "title" shows up in the auto-generated docs at http://localhost:8000/docs
app = FastAPI(title="RAG Platform API")

# Add CORS middleware to the app.
# Middleware is code that runs on EVERY request before it reaches your endpoint.
# Think of it as a security guard at the door that checks every visitor.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Which websites can call our API. "*" means any website (fine for development, restrict in production)
    allow_methods=["*"],   # Which HTTP methods are allowed (GET, POST, PUT, DELETE, etc). "*" means all of them
    allow_headers=["*"],   # Which HTTP headers are allowed in requests. "*" means all of them
)

# Register the chat router with our app. This adds all the endpoints defined in chat.py (the /chat endpoint).
# include_router is how FastAPI lets you split endpoints across multiple files instead of putting everything in main.py.
app.include_router(chat_router)


# Define a simple GET endpoint at /health.
# @app.get("/health") is a "decorator" - it tells FastAPI: "when someone visits /health, run this function"
# This is useful for quickly checking if the server is running (e.g., from a browser or monitoring tool).
@app.get("/health")
def health():
    # Return a JSON response. FastAPI automatically converts Python dicts to JSON.
    return {"status": "ok"}
