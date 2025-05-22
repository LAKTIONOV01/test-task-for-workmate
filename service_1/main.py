import uvicorn
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()
app.title = 'Service 1'


def check_service_availability(url: str) -> bool:
    ok = False
    try:
        req = requests.get(url)
        if req.status_code == 200:
            ok = True
    except requests.exceptions.RequestException as e:
        print(e)
    return ok

@app.get('/')
def root():
    return {'msg': 'Service 1 root'}

@app.post('/to-service-2')
def to_serivce_2():
    if not check_service_availability('http://127.0.0.1:8002/'):
        raise HTTPException(status_code=404, detail='Service 2 not work')
    response = requests.post('http://127.0.0.1:8002//response-from-service-2')
    print(response.json())
    return response.json()


@app.post('/to-service-3')
def to_serivce_3():
    if not check_service_availability('http://127.0.0.1:8003/'):
        raise HTTPException(status_code=404, detail='Service 3 not work')
    response = requests.post('http://127.0.0.1:8003//response-from-service-3')
    print(response.json())
    return response.json()


if __name__ == '__main__':
    uvicorn.run(app, port=8001)