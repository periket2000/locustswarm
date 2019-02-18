import logging
from flask_restplus import Api
import socket
from modules import __title__ as title, __description__ as desc

hostname = socket.gethostname()
log = logging.getLogger(__name__)
api = Api(version='1.0', title=title,
          description=desc)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500
