""" Custom exceptions for the application. """

class APIError(Exception):
    """ Indicates that a third party has returned an error response. """

    def __init__(self, message=None, status_code=None):
        super(APIError, self).__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message + ' (status code ' + str(self.status_code) + ')'
