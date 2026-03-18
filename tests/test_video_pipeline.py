from utils.helpers import processing

def test_full_pipeline(client):
   
    res = client.post("/api/videos", {"title": "Video Test"})
    assert res.status_code == 201

    data = res.json()
    assert "id" in data
    assert data["id"] is not None

    video_id = data["id"]


    res = client.post(f"/api/videos/{video_id}/process-captions")
    assert res.status_code == 202

    
    assert processing(client, video_id)

    res = client.get(f"/api/captions?videoId={video_id}")
    assert res.status_code in [200, 204]

    data = res.json() if res.status_code == 200 else []

    
    if isinstance(data, list):
       raise AssertionError("Bug: Captions API returned list instead of object")

    else:
        assert "text" in data
        assert isinstance(data["text"], str)
        assert len(data["text"]) > 0

    
    res = client.delete(f"/api/videos/{video_id}")
    assert res.status_code in [200, 204]