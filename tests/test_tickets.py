from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_ticket():
    response = client.post(
        "/tickets/",
        json={"title": "Title create ticket",
              "description": "Description create ticket"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Title create ticket"
    assert data["description"] == "Description create ticket"
    assert data["status"] == "open"
    assert "id" in data
    assert "created_at" in data


def test_list_tickets():
    client.post(
        "/tickets/",
        json={"title": "Title list tickets", "description": "Description list tickets"},
    )
    response = client.get("/tickets/")
    print(response)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_ticket():
    created = client.post(
        "/tickets/",
        json={"title": "Title get ticket", "description": "Description get ticket"},
    ).json()

    response = client.get(f"/tickets/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_get_ticket_not_found():
    response = client.get("/tickets/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"


def test_update_ticket():
    created = client.post(
        "/tickets/",
        json={"title": "Old title", "description": "Old Description"},
    ).json()

    response = client.put(
        f"/tickets/{created['id']}",
        json={
            "title": "New title",
            "description": "New Description",
            "status": "stalled",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New title"
    assert data["description"] == "New Description"
    assert data["status"] == "stalled"


def test_update_ticket_not_found():
    response = client.put(
        "/tickets/99999",
        json={
            "title": "New title",
            "description": "New Description",
            "status": "stalled",
        },
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"


def test_close_ticket():
    created = client.post(
        "/tickets/",
        json={"title": "Title close ticket", "description": "Description close ticket"},
    ).json()

    response = client.patch(f"/tickets/{created['id']}/close")
    assert response.status_code == 200
    assert response.json()["status"] == "closed"


def test_close_ticket_not_found():
    response = client.patch("/tickets/99999/close")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"