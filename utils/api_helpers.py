import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def create_post(title, body, user_id):
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    return requests.post(f"{BASE_URL}/posts", json=payload)

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

def update_post(post_id, title, body, user_id):
    payload = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)

def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")
