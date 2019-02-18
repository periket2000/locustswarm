import sys
import os

def api():
    from api.api import app
    port = int(os.getenv("API_PORT", 5000))
    server_name = os.getenv("API_HOST", "0.0.0.0")
    debug = False
    application = app()
    application.run(server_name, port, debug)
    sys.exit(0)

if __name__ == '__main__':
    api()
