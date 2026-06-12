def test_create_student(client):
    response = client.post(
        "/students",
        json={"name": "Test User", "reg_no": "12345"}
    )
    assert response.status_code == 200
    assert response.json()["reg_no"] == "12345"

def test_get_students(client):
    client.post("/students", json={"name": "Alice", "reg_no": "111"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_student_by_reg_no(client):
    client.post("/students", json={"name": "Bob", "reg_no": "222"})
    response = client.get("/students/222")
    assert response.status_code == 200
    assert response.json()["name"] == "Bob"

def test_get_student_not_found(client):
    response = client.get("/students/999")
    assert response.status_code == 404
