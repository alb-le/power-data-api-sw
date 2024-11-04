class SwApiError(Exception):
    """There was a problem with the SW API"""
    def __init__(self, msg):
        super().__init__(msg)

class SwApiNotFoundError(Exception):
    """Raise when there is a problem with the SW API"""
    def __init__(self, msg):
        super().__init__(msg)