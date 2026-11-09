# Another user cannot read someone else's rating.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    print("read:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot change someone else's rating.
def test_other_user_cannot_change_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print("change:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == 3


# Another user cannot delete someone else's rating.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    print("delete:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating