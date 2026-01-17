import subprocess
import uvicorn
import httpx
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/stock")
def open_stock(data: dict):
    name = data.get("name", "")
    script = f'''
    set the clipboard to "{name}"
    tell application "System Events"
        key code 49 using command down -- Cmd+Space 打开 Spotlight
        delay 0.1
        key code 9 using command down -- Cmd+V 粘贴
        delay 0.5 -- 等待 Spotlight 检索
        -- 手动回车
    end tell
    '''
    subprocess.run(["osascript", "-e", script])
    return {"ok": True}
    
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(request: Request, path: str):
    async with httpx.AsyncClient() as client:
        url = f"http://localhost:8002/{path}"
        response = await client.request(
            method=request.method,
            url=url,
            headers=dict(request.headers),
            content=await request.body()
        )
        return Response(content=response.content, status_code=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7002)
	