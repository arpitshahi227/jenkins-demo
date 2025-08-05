from utils.api_helpers import create_post, get_post, update_post, delete_post


sample_title = "Sample Jenkins"
sample_body = "Test post body"

def test_create_post():
    response = create_post(sample_title, sample_body, 1)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == sample_title
    assert data["body"] == sample_body
    assert data["userId"] == 1

def test_get_post():
    response = get_post(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
