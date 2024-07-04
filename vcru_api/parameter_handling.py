from enum import Enum
from typing import Any, Callable


class Sorting(Enum):
    NEW = "new"
    POPULAR = "popular"
    HOTNESS = "hotness"
    DATE = "date"
    FROM_MINUS_10 = "from-10"
    FROM_5 = "from5"
    FROM_10 = "from10"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    ALL = "all"


class PageName(Enum):
    POPULAR = "popular"
    NEW = "new"
    MY = "my"


class InvalidParameterError(ValueError):
    """
    Raised when a parameter value is invalid.
    """

    def __init__(self, parameter, message: str):
        self.parameter = parameter
        self.message = f"The '{self.parameter}' parameter {message}"
        super().__init__(self.message)


def bool_to_str(value: bool) -> str:
    return "true" if value else "false"


def validate_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to validate arguments of a function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if "markdown" in kwargs:
            markdown = kwargs["markdown"]
            if isinstance(markdown, bool):
                markdown = bool_to_str(markdown)
            if markdown.lower() not in ["true", "false"]:
                raise InvalidParameterError(
                    "markdown", "parameter must be a string 'true' or 'false'"
                )
            kwargs["markdown"] = markdown

        if "firstLoad" in kwargs:
            firstLoad = kwargs["firstLoad"]
            if isinstance(firstLoad, bool):
                firstLoad = bool_to_str(firstLoad)
            if firstLoad.lower() not in ["true", "false"]:
                raise InvalidParameterError(
                    "firstLoad", " must be a string 'true' or 'false'"
                )
            kwargs["firstLoad"] = firstLoad

        if "sorting" in kwargs:
            sorting = kwargs["sorting"]
            if sorting not in [e.value for e in Sorting]:
                raise InvalidParameterError(
                    "sorting",
                    f"must be one of the following: {', '.join([e.value for e in Sorting])}",
                )

        if "pageName" in kwargs:
            pageName = kwargs["pageName"]
            if pageName not in [e.value for e in PageName]:
                raise InvalidParameterError(
                    "pageName",
                    f"must be one of the following: {', '.join([e.value for e in PageName])}",
                )

        if "contentId" in kwargs:
            contentId = kwargs["contentId"]
            if not isinstance(contentId, int):
                raise InvalidParameterError("contentId", "must be an integer")

        if "id" in kwargs:
            id = kwargs["id"]
            if not isinstance(id, int):
                raise InvalidParameterError("id", "must be an integer")

        return func(*args, **kwargs)

    return wrapper
