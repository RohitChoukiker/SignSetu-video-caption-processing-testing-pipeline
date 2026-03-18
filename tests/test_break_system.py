from utils.helpers import processing


def test_double_processing(client):
    res = client.post("/api/videos", {"title": "test"})
    video_id = res.json()["id"]

    res1 = client.post(f"/api/videos/{video_id}/process-captions")
    res2 = client.post(f"/api/videos/{video_id}/process-captions")

    assert res2.status_code != 200, "Bug: duplicate processing allowed"
    
    
def test_captions_before_processing(client):
    res = client.post("/api/videos", {"title": "test"})
    video_id = res.json()["id"]

    res = client.get(f"/api/captions?videoId={video_id}")

    assert res.status_code != 200, "Bug: captions available before processing"
    
    
    
def test_delete_during_processing(client):
    res = client.post("/api/videos", {"title": "test"})
    video_id = res.json()["id"]

    client.post(f"/api/videos/{video_id}/process-captions")

    res = client.delete(f"/api/videos/{video_id}")

    assert res.status_code != 200, "Bug: deletion allowed during processing"        
    
    
    
    
def test_repeatability(client):
    for _ in range(2):
        res = client.post("/api/videos", {"title": "repeat"})
        video_id = res.json()["id"]

        client.post(f"/api/videos/{video_id}/process-captions")
        assert processing(client, video_id)

        res = client.get(f"/api/captions?videoId={video_id}")
        assert res.status_code == 200

        client.delete(f"/api/videos/{video_id}")    