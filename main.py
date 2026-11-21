
# ==========================================
# BASIC FASTAPI WEB API
# ==========================================

from fastapi import FastAPI

# Step 1: Create FastAPI application

app = FastAPI(
    title="My First FastAPI App",
    description="A beginner-friendly FastAPI project",
    version="1.0.0"
)


# Step 2: Root endpoint (GET /)

@app.get("/")
def home():

    return {
        "message": "Hello, FastAPI"
    }


# Step 3: Path parameter endpoint (GET /greet/{name})

@app.get("/greet/{name}")
def greet_user(name: str):

    return {
        "message": f"Hello, {name}!",
        "name": name
    }


# Step 4: Query parameter endpoint (GET /welcome?name=Dinesh)

@app.get("/welcome")
def welcome_user(name: str = "Guest"):

    return {
        "message": f"Welcome, {name}!"
    }


# Step 5: Health check endpoint (GET /health)

@app.get("/health")
def health_check():

    return {
        "status": "success",
        "message": "API is running"
    }
