import pytest
from vcru_api.sync_wrapper import VCRUAPISync


def test_get_feed():
    with VCRUAPISync() as api:
        feed = api.get_feed()
        assert isinstance(feed, dict)


def test_get_recommendations():
    with VCRUAPISync() as api:
        recommendations = api.get_recommendations(contentId=1279222)
        assert isinstance(recommendations, dict)


def test_get_comments():
    with VCRUAPISync() as api:
        comments = api.get_comments(contentId=1279222)
        assert isinstance(comments, dict)


def test_get_content():
    with VCRUAPISync() as api:
        content = api.get_content(id=962873)
        assert isinstance(content, dict)


def test_get_distribution():
    with VCRUAPISync() as api:
        distribution = api.get_distribution()
        print(distribution)
        assert isinstance(distribution, dict)


def test_get_subsite():
    with VCRUAPISync() as api:
        subsite = api.get_subsite()
        assert isinstance(subsite, dict)
