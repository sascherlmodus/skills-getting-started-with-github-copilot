from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_names = set(activities.keys())

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    assert set(response.json().keys()) == expected_activity_names