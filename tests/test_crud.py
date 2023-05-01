from fastapi.testclient import TestClient
from Lagoa.main import app


client = TestClient(app)


class TestCrud:
    def test_nome(self):
        assert 1 == 1

    def _test_create(self):
        payload = {"name":"leite", "price":4.80}
        response = client.post("/product/", json=payload)
        products = response.json()
        assert response.status_code == 201
        assert products == {"name":"leite", "price":4.80}

    def _test_list(self):
        response = client.get("/product/")
        products = response.json()
        assert response.status_code == 200
        assert products == [{"name":"leite", "price":4.80}]

    def _test_update(self):
        payload = {"price":5.00}
        response = client.put("/product/123", json=payload)
        products = response.json()
        assert response.status_code == 200
        assert products == {"name":"leite", "price":5.00}

    def _test_detail(self):
        response = client.get("/product/123")
        products = response.json()
        assert response.status_code == 200
        assert products == {"name":"leite", "price":4.80}

    def _test_delete(self):
        pass