import time

def processing(client, video_id, timeout=30):
    start = time.time()

    while time.time() - start < timeout:
        res = client.get(f"/api/videos/{video_id}")

        if res.status_code != 200:
            time.sleep(1)
            continue

        status = res.json().get("status", "").lower()

        if status in ["completed", "processed", "done"]:
            return True

        time.sleep(2)

    raise AssertionError("Processing timeout async failure")