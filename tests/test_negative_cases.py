def test_invalid_video_id(client):
    res = client.get("/api/videos/999999")
    assert res.status_code in [400, 401, 404]


def test_double_delete(client):
    res = client.post("/api/videos", {"title": "test"})
    video_id = res.json()["id"]

    client.delete(f"/api/videos/{video_id}")
    res = client.delete(f"/api/videos/{video_id}")

    assert res.status_code != 200 

def test_missing_auth():
    import requests
    res = requests.get("https://qa-testing-navy.vercel.app/api/videos")
    assert res.status_code in [400, 401, 403]


def test_process_without_create(client):
    res = client.post("/api/videos/123/process-captions")
    assert res.status_code != 200