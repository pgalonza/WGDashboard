import multiprocessing
import dashboard

app_host, app_port = dashboard.get_host_bind()
if ':' in app_host:
    app_host = f'[{app_host}]'

worker_class = 'gthread'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
bind = f"{app_host}:{app_port}"
daemon = True
pidfile = './gunicorn.pid'
