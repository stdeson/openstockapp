run:
	uv run main.py
start:
	pm2 start "uv run main.py" --name openstockapp
stop:
	pm2 stop openstockapp
restart:
	pm2 restart openstockapp
logs:
	pm2 logs openstockapp
