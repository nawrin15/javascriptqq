from fastapi import FastAPI, Response
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import time
import json, uvicorn
from asyncio import sleep

app = FastAPI()

@app.get('/')
def root(request):
    return {"hello": "world"}


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def fake_video_streamer():
    for i in range(10):
        await sleep(1)
        yield b"some fake video bytes"


@app.get("/stream")
async def type1():
    return StreamingResponse(fake_video_streamer(),  media_type="text/event-stream")


some_file_path = "abc.mp4"


@app.get("/stream2")
def type2():
    def iterfile():  # 
        with open(some_file_path, mode="rb") as file_like:  # 
            yield from file_like  # 

    return StreamingResponse(iterfile(), media_type="video/mp4")

async def waypoints_generator():
    waypoints = open('waypoints.json')
    waypoints = json.load(waypoints)
    for waypoint in waypoints[0: 10]:
        data = json.dumps(waypoint)
        yield f"event: locationUpdate\ndata: {data}\n\n"
        await sleep(1)

@app.get("/get-waypoints")
async def root():
    return StreamingResponse(waypoints_generator(), media_type="text/event-stream")

async def data_generator():
    while True:
        await sleep(1)
        yield f'data: {datetime.now().second} \n\n'
    
@app.get("/ppp")
async def root2():
    return StreamingResponse(data_generator(), media_type="text/event-stream")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8088)
