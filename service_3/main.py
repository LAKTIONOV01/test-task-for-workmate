import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.title = 'Service 3'


@app.get('/')
def root():
    return {'msg': 'Service 3 root'}

@app.post('/response-from-service-3')
def response_from_service_2():
    return {'msg': 'response from Service 3'}


if __name__ == '__main__':
    uvicorn.run(app, port=8003)