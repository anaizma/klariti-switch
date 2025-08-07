from fastapi import FastAPI #basically importing FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()  #this is creating a webserver app and where you'll define what it should do

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://klariti-switch.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") #so this basically says that if someone visits the homepage (/) using GET (like typing it into a browser), then you do this
def read_root(): #this is defining a function
    return {"message": "Hello from Klariti backend!"}  # this is what the server sends back to the browser
#also its in a formart called JSON^^



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("klariti-backend.main:app", host="0.0.0.0", port=8080)

