import uvicorn
from fastapi import FastAPI

app = FastAPI()

def sum(num1, num2):
    return num1+num2

@app.get('/')
def main():
    return {'Message': 'Hello World!'}

@app.get('/route-test')
def route_test():
    return {'Message': 'Route test!'}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')

