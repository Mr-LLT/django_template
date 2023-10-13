import os

BASE_DIR = os.path.dirname(__file__)
BASE_NAME = os.path.split(BASE_DIR)[-1]

OK = '\033[1;4;32;40mOK\033[0m'


# Configure templates. (uwsgi & nginx)

UWSGI_FILE = "{{project_name}}.ini"
UWSGI_CONF = """
[uwsgi]
threads = 1
processes = 1
master = true
vacuum = true
socket = /tmp/{{project_name}}.sock
pidfile = /tmp/{{project_name}}.pid
chdir = {{project_directory}}
module = {{project_name}}.wsgi:application
daemonize = /var/log/uwsgi/{{project_name}}.log
"""

NGINX_FILE = "{{project_name}}.conf"
NGINX_CONF = """
server {
    listen      %(listen_port)s;
    server_name %(server_name)s;
    set         $base {{project_directory}};

    location /media/ {
        alias $base/www/upload/;
    }

    location /static/ {
        alias $base/www/static/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass /tmp/{{project_name}}.sock;
        uwsgi_param UWSGI_SCRIPT {{project_name}}.wsgi;
        uwsgi_param UWSGI_CHDIR $base/{{project_name}};
    }
}
"""


# Starting deployment.

os.environ['PRODUCTION'] = 'True'
if 'DJANGO_SECRET_KEY' not in os.environ:
    secret_key = input('Enter secret key:').strip()
    os.environ['DJANGO_SECRET_KEY'] = secret_key

server_name = input("Enter server name: ").lower().strip()
listen_port = input("Enter listen port: ").lower().strip()

if server_name and listen_port: 
    NGINX_CONF = NGINX_CONF % dict(
        server_name=server_name, listen_port=listen_port
    )
    os.system(f'cat > {UWSGI_FILE} << EOF{UWSGI_CONF}EOF')
    os.system(f'cat > {NGINX_FILE} << EOF{NGINX_CONF}EOF')
else: raise ValueError('Bad value.')

NGINX_PATH = f'/etc/nginx/conf.d/{NGINX_FILE}'
os.system(f'sudo link {NGINX_FILE} {NGINX_PATH}')
os.system(f'uwsgi --ini {UWSGI_FILE}')
os.system('sudo service nginx restart')

msg = f'Please open the link in browser.'\
    f'\n\t- http://{server_name}:{listen_port}/'
print(f'\n{msg.strip()}\n{OK}')
