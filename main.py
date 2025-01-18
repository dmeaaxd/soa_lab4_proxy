import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.fastapi_app:app", host="localhost", port=8910, reload=True)

