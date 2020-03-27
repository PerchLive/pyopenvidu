# Base exception


class OpenViduError(BaseException):
    pass

# Universal error:


# Session errors

class OpenViduSessionError(OpenViduError):
    pass


class OpenViduSessionDoesNotExistsError(OpenViduSessionError):
    pass


# Connection errors

class OpenViduConnectionError(OpenViduError):
    pass


class OpenViduConnectionDoesNotExistsError(OpenViduConnectionError):
    pass