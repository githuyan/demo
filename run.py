import uvicorn


if __name__ == '__main__':
    uvicorn.run('demo:app', host='0.0.0.0', port=8900, reload=True)
