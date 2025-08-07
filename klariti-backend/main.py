from fastapi import FastAPI #basically importing FastAPI

app = FastAPI()  #this is creating a webserver app and where you'll define what it should do

@app.get("/") #so this basically says that if someone visits the homepage (/) using GET (like typing it into a browser), then you do this
def read_root(): #this is defining a function
    return {"message": "Hello from Klariti backend!"}  # this is what the server sends back to the browser
#also its in a formart called JSON^^
