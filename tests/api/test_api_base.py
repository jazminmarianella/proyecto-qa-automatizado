import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # ejemplo de API pública

def test_get_posts_status_code():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_post_id_1():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1

