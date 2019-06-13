from api.v1.models.Error import NotFoundError
from api.v1.models.Error import InternalServerError
from api.v1.models.Error import AccessDeniedError
from api.v1.models.Error import UnauthorizedError

from api.v1.views.ErrorView import ErrorView

ErrorView = ErrorView()


def handle_page_not_found():
    error = NotFoundError("Page")
    return ErrorView.display(error)


def handle_internal_server_error():
    error = InternalServerError()
    return ErrorView.display(error)


def handle_access_denied_error():
    error = AccessDeniedError()
    return ErrorView.display(error)


def handle_unauthorized_error():
    error = UnauthorizedError()
    return ErrorView.display(error)
