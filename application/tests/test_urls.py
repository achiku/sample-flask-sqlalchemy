# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('url, status_code', [
    ('/api/items/',  200),
    ('/api/items/{item_id}/',  200),
    ('/api/items/history/', 200),
])
def test_api_request(url, status_code, test_client, api_url_data):
    url_str = url.format(item_id=api_url_data['single_item_id'])
    res = test_client.get(url_str)
    assert res.status_code == status_code
