from ninja import Body, Form, NinjaAPI
from ninja.testing import TestClient

api = NinjaAPI()

# testing Body marker:
client = TestClient(api)


@api.post("/body")
def create_body(request, start: int = Body(...)):
    return [start]


@api.post("/bodies")
def create_bodies(request, start: int = Body(...), end: int = Body(...)):
    return [start, end]


@api.post("/body-form")
def create_body_form(request, start: int = Body(2), end: int = Form(1)):
    return [start, end]


def test_one_body():
    assert client.post("/body", json={"start": 1}).json() == [1]


def test_two_bodies():
    assert client.post("/bodies", json={"start": 1, "end": 2}).json() == [1, 2]


def test_body_form():
    assert client.post("/body-form", POST={"start": "1", "end": "2"}).json() == [1, 2]
    assert client.post("/body-form").json() == [2, 1]
