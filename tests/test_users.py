def test_create_user(client):

    response = client.post(
        "/users",
        json={
            "name": "Kunal",
            "email": "kunal@example.com"
        }
    )

    assert response.status_code == 201

    assert response.json[
        "name"
    ] == "Kunal"
