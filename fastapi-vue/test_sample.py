import requests

username = "user1"

def test_register_user():
    url = "http://localhost:5000/register"
    data = {
        "username": f"{username}",
        "password": "testpassword"
    }
    response = requests.post(url, json=data)

    print(response.json())
    assert response.status_code == 200
    assert response.json()["username"] == f"{username}"
    

def test_login_user_fail():
    url = "http://localhost:5000/login"
    data = {
        "username": "user1",
        "password": "wrongpassword"
    }
    response = requests.post(url, data=data)

    assert response.status_code == 401
    assert "Authorization" not in response.cookies

def test_login_user_success():
    response = login()
    auth = response.cookies["Authorization"]

    url = "http://localhost:5000/users/whoami"
    response = requests.get(url, cookies={"Authorization": auth})
    assert response.status_code == 200
    assert response.json()["username"] == "user1"

def test_messages():
    response = login()
    auth = response.cookies["Authorization"]

    url = "http://localhost:5000/messages"
    data = {
        "message": "Hello, world!"
    }
    response = requests.post(url, json=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, world!"

    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == ["Hello, world!"]

    url = "http://localhost:5000/message/1"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, world!"

    url = "http://localhost:5000/message/0"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json()["detail"] == "Message 0 not found"

    response = requests.delete(url)
    assert response.status_code == 200
    assert response.json()["message"] == "Deleted message 1"

def test_login_delete_user():
    response = login()
    auth = requests.get(url, cookies={"Authorization": auth})
    # print(response.json())


    userId = 1
    url = f"http://localhost:5000/user/{userId}"
    response = requests.delete(url, cookies={"Authorization": auth})
    assert response.status_code == 200
    assert response.json()["message"] == f"Deleted user {userId}"

def login():
    url = "http://localhost:5000/login"
    data = {
        "username": "user1",
        "password": "testpassword"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert "Authorization" in response.cookies
    return response