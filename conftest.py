import pytest

@pytest.fixture(scope="session")
def auth_creds():
    return ("standard_user", "secret_sauce")
