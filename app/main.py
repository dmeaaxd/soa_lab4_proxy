import uvicorn

if __name__ == '__main__':
    uvicorn.run("fastapi_app:app", host="localhost", port=8910, reload=True)

