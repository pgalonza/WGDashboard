import dashboard

app_host, app_port = dashboard.get_host_bind()
if ':' in app_host:
    app_host = f'[{app_host}]'

bind = f"{app_host}:{app_port}"
daemon = True
pidfile = './gunicorn.pid'
