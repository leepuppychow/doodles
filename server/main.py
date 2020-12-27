from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def home():
  return {'message': 'Things are ok!'}