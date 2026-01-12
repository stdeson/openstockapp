import subprocess
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.post("/stock")
def open_stock(data: dict):
    name = data.get("name", "")
    script = f'''
    tell application "System Events"
        key code 49 using command down
        delay 0.3
        keystroke "{name}"
        delay 0.2
        key code 36
    end tell
    '''
    subprocess.run(["osascript", "-e", script])
    return {"ok": True}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
	