# APIRouter lets us define endpoints in a separate file instead of putting everything in main.py.
# We create a router here, define endpoints on it, then register it in main.py with app.include_router().
from fastapi import APIRouter

# BaseModel is from Pydantic (a data validation library that comes with FastAPI).
# We use it to define the shape of request and response data.
# FastAPI will automatically validate incoming JSON against these models and reject bad requests.
from pydantic import BaseModel

# The 'requests' library lets us make HTTP calls to other services (in this case, Ollama's API).
# This is different from FastAPI's "request" - this is for our backend to call OTHER APIs.
import requests

# Create a router instance. Endpoints defined on this router will be added to the main app in main.py.
router = APIRouter()

# The URL where Ollama's API is running. Ollama exposes a REST API on port 11434.
# /api/generate is the endpoint that takes a prompt and returns a generated response.
OLLAMA_URL = "http://localhost:11434/api/generate"

# Which model to use. This must match a model you've pulled with 'ollama pull'.
# We pulled llama3.2 earlier, so that's what we use here.
MODEL = "llama3.2"


# This class defines what the request body must look like.
# If someone sends a POST to /chat, their JSON must have a "message" field that's a string.
# Example valid request: {"message": "What is RAG?"}
# Example invalid request: {"msg": "hello"} -> FastAPI returns a 422 error automatically
class ChatRequest(BaseModel):
    message: str


# This class defines what our response will look like.
# FastAPI uses this to validate our response and generate documentation.
class ChatResponse(BaseModel):
    answer: str  # The LLM's response text
    model: str   # Which model generated the response


# This decorator registers a POST endpoint at /chat on our router.
# response_model=ChatResponse tells FastAPI the response shape (used for docs and validation).
# POST is used (instead of GET) because we're sending data (the message) to the server.
@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # req is automatically parsed from the JSON body. FastAPI sees the type hint (ChatRequest)
    # and validates the incoming JSON against it. If valid, req.message contains the user's message.

    # Send an HTTP POST request to Ollama's /api/generate endpoint.
    # json={...} sends the data as a JSON body (not form data).
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,         # Tell Ollama which model to use
        "prompt": req.message,  # The user's question/message
        "stream": False,        # Get the full response at once (not word-by-word streaming)
    })

    # Parse Ollama's JSON response into a Python dictionary.
    # Ollama returns something like: {"response": "The answer is...", "done": true, ...}
    data = response.json()

    # Build and return our ChatResponse. FastAPI converts this to JSON automatically.
    # data["response"] is where Ollama puts the generated text.
    return ChatResponse(answer=data["response"], model=MODEL)
