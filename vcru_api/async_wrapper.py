import aiohttp
from .parameter_handling import validate_args


class VCRUAPIAsync:
    """
    A simple asynchronous API wrapper for the vc.ru service.
    """

    def __init__(self, base_url="https://api.vc.ru"):
        """
        Initialize the API wrapper.
        """
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    @validate_args
    async def get_feed(self, markdown="false", sorting="hotness", pageName="popular"):
        """
        Get the feed from vc.ru.

        Parameters:
        - markdown: a boolean indicating whether to return markdown or not ('false', 'true').
        - sorting: a string indicating the sorting method ('new', 'hotness', 'day', 'week', 'month', 'year', 'all', 'from-10', 'from5', 'from10').
        - pageName: a string indicating the page name ('popular', 'new', 'my').
        """
        params = {"markdown": markdown, "sorting": sorting, "pageName": pageName}

        async with self.session.get(
            f"{self.base_url}/v2.5/feed", params=params
        ) as response:
            return await response.json()

    @validate_args
    async def get_recommendations(self, markdown="false", contentId=None):
        """
        Get the recommendations from vc.ru.

        Parameters:
        - markdown: a boolean indicating whether to return markdown or not ('false', 'true').
        - contentId: an integer indicating the content ID for which to get recommendations.
        """
        params = {"markdown": markdown, "contentId": contentId}
        async with self.session.get(
            f"{self.base_url}/v2.5/recommendations", params=params
        ) as response:
            return await response.json()

    @validate_args
    async def get_comments(self, sorting="hotness", contentId=None, firstLoad=True):
        """
        Get the comments from vc.ru.

        Parameters:
        - sorting: a string indicating the sorting method ('hotness', 'date').
        - contentId: an integer indicating the content ID for which to get comments.
        - firstLoad: a boolean indicating whether this is the first load.
        """
        params = {"sorting": sorting, "contentId": contentId, "firstLoad": firstLoad}
        async with self.session.get(
            f"{self.base_url}/v2.5/comments", params=params
        ) as response:
            return await response.json()

    @validate_args
    async def get_content(self, id=None, markdown="true"):
        """
        Get the content from vc.ru.

        Parameters:
        - id: an integer indicating the content ID to get. (the post id)
        - markdown: a boolean indicating whether to return markdown or not.
        """
        params = {"id": id, "markdown": markdown}
        async with self.session.get(
            f"{self.base_url}/v2.5/content", params=params
        ) as response:
            return await response.json()

    # @validate_args
    async def get_distribution(self, place="header"):
        """
        Get the distribution from vc.ru. (advertisement)

        Parameters:
        - place: a string indicating the place.
        """
        params = {
            "place": place,
        }
        async with self.session.get(
            f"{self.base_url}/v2.5/distribution", params=params
        ) as response:
            return await response.json()

    # @validate_args
    async def get_subsite(self, uri="crypto", markdown=False):
        """
        Get the subsite from vc.ru.

        Parameters:
        - uri: a string indicating the uri of the subsite. (https://vc.ru/discovery/topics)
        - markdown: a boolean indicating whether to return markdown or not.
        """
        params = {"uri": uri, "markdown": markdown}
        async with self.session.get(
            f"{self.base_url}/v2.7/subsite", params=params
        ) as response:
            return await response.json()
