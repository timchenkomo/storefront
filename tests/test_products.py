from starlette.testclient import TestClient

from main import APP

client = TestClient(APP)


def test_read_products_index():
    response = client.get("/products")
    assert response.status_code == 200
