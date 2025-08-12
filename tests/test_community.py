def test_community_feed(client):
    rv = client.get('/community/feed')
    assert rv.status_code == 200
