import pytest
from http_web_client import client


def test_fetch_json():
    status, body, text = client.fetch("https://httpbin.org/get")
    assert status == 200
    assert isinstance(text, str)
    assert isinstance(body, dict)
    assert "url" in body
