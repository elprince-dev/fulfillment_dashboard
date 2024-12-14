from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import get_inventory_data, get_defect_trends
import psycopg2
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow requests from specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Database connection setup
def connect_db():
    conn = psycopg2.connect(
        dbname='warehouse',  
        user='postgres',       
        password='asdASD123123',  
        host='172.29.48.1',       
        port='5433'
    )
    return conn

@app.get("/inventory")
async def inventory():
    conn = connect_db()
    data = get_inventory_data(conn)
    conn.close()
    return JSONResponse(content=data)

@app.get("/defects")
async def defects():
    conn = connect_db()
    data = get_defect_trends(conn)
    conn.close()
    return JSONResponse(content=data)
