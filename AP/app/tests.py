from src import main
from unittest import TestCase
from fastapi.testclient import TestClient

client = TestClient(main)

class Test(TestCase):
    def test_sum1(self):
        result = app.sum(1,2)
        self.assertEqual(result, 3)

    def test_sum2(self):
        result = app.sum(-1, 0)
        self.assertEqual(result, -1)

    def test_sum2(self):
        result = app.sum(10,-2)
        self.assertEqual(result, 8)

    def test_main_route(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Message", "Hello World!"})

    def test_route_test_route(self):
        response = client.get("/test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Message", "Route test!"})


