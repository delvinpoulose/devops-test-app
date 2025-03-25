from fastapi import FastAPI, Request
import socket
import mysql.connector
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

# DB Connection
db = mysql.connector.connect(
    host="172.31.33.72",
    user="root",
    password="root",
    database="hostlogs",
    auth_plugin='caching_sha2_password'
)

@app.get("/hostname")
def get_hostname(request: Request):
    hostname = socket.gethostname()
    ip = request.client.host
    timestamp = datetime.now()

    cursor = db.cursor()
    cursor.execute("INSERT INTO request_log (ip_address, hostname, timestamp) VALUES (%s, %s, %s)",
                   (ip, hostname, timestamp))
    db.commit()
    cursor.close()

    return {"hostname": hostname}

