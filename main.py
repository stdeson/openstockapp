import subprocess
import uvicorn
from fastapi import FastAPI

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
        delay 1 -- 等待 Spotlight 检索
        key code 36 -- 回车
    end tell
    '''
    subprocess.run(["osascript", "-e", script])
    return {"ok": True}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
	