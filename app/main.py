from fastapi import FastAPI

app = FastAPI(title="CyVox Server")

@app.get('/')
def read_root():
    return {"Server Says": "Hello World!"}

@app.get('/post/unpublished')
def unpunlished_posts():
    return {"data": "all unpublihsed posts"}

@app.get('/post/{id}')
def post_data(id: int):
    return {"data": id}

@app.get('/post/voice/add/{id}')
def post_data(id: int):
    return {"voiceId": id, "message": "Voice recieved"}

