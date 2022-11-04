import pytest
from app import create_app


### RAN OUT OF TIME FOR UNIT TESTING ###
@pytest.fixture
def client():
    # Prepare before your test
    app = create_app()

    with app.test_client() as client:
        yield client


# def test_square(client):
#     rv = client.get("/pjm_projects?state=NV")
#     assert b["64"] == rv.data
