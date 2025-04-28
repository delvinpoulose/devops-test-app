from fastapi import FastAPI, Request
import socket
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",              # for local dev
        "https://delvin.projectcaffe.shop"    # your deployed frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hostname")
def get_hostname(request: Request):
    hostname = socket.gethostname()
    ip = request.client.host
    timestamp = datetime.now()

    # Just return data, no DB insert
    return {
        "hostname": hostname,
        "ip_address": ip,
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }
