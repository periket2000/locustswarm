from modules.utils.config import get_log

# log config
logger_name = __name__
logger = get_log(log_name=logger_name)


def error(msg):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            # caller = args[0] ==> wrapped function first param: self
            try:
                return function(*args, **kwargs)
            except Exception as e:
                logger.exception(e)
                return {'reason': msg}, 404
        # if we don't add this line below, we lose Implementation Notes on the swagger api.
        wrapper.__doc__ = function.__doc__
        return wrapper
    return real_decorator