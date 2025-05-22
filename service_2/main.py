import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.title = 'Service 2'


@app.get('/')
def root():
    return {'msg': 'Service 2 root'}

@app.post('/response-from-service-2')
def response_from_service_2():
    return {'msg': 'response from Service 2'}


if __name__ == '__main__':
    uvicorn.run(app, port=8002)