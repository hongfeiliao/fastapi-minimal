from fastapi import FastAPI, Body, Response

app = FastAPI(title='minimal fastapi')

@app.get('/health')
async def health():
    return {'ok': True}

@app.post('/echo')
async def echo(text: str = Body(..., media_type='text/plain')):
    return Response(content=text, media_type='text/plain')
