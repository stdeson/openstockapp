run:
	uv run main.py
start:
	pm2 start "/Users/ws/bin/ngrok http 7002" --name ngrok
	pm2 start "uv run main.py" --name openstockapp
stop:
	pm2 stop ngrok openstockapp
restart:
	pm2 restart ngrok openstockapp
logs:
	pm2 logs
