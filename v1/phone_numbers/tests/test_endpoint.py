import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


base_url = "/v1/phone-numbers"


@pytest.mark.parametrize("phone_number", [
    "1%20212%205690123",  # => 1 212 5690123
    "%2B1212%205690123",  # => +1212 5690123
    "%2B12125690123",  # => +12125690123
    "12125690123"  # => 12125690123
])
def test_get_information_valid_phone_number(client, phone_number):
    # test valid phone number
    response = client.get(base_url, params=f"phoneNumber={phone_number}")

    assert response.status_code == 200
    assert response.json() == {
        "phoneNumber": "+12125690123",
        "countryCode": "US",
        "areaCode": "212",
        "localPhoneNumber": "5690123"
    }


@pytest.mark.parametrize("phone_number", [
    "1-212-569-0123",
    "1 (212) 5690123",
    "1    212    5690123",
    "1 2 1 2 5 6 9 0 1 2 3"
])
def test_get_error_invalid_phone_number(client, phone_number):
    # test invalid phone number without contry code
    response = client.get(
        base_url,
        params=f"phoneNumber={phone_number}"
    )
    # test valid phone number without country code
    response = client.get(base_url, params=f"phoneNumber={phone_number}")
    assert response.status_code == 200
    response = response.json()
    assert response["status_code"] == 422
    assert response["detail"]["error"] == {
        "phoneNumber": "phone number does not match E.164 format: [+][country code][area code][local phone number]"
    }


@pytest.mark.parametrize("phone_number,country_code", [
    ("2125690123", "US"),
    ("2125690123", "MX"),
])
def test_get_information_valid_phone_number_with_country_code(client, phone_number, country_code):
    # test valid phone number with contry code
    response = client.get(
        base_url,
        params=f"phoneNumber={phone_number}&countryCode={country_code}"
    )

    assert response.status_code == 200
    assert response.json()["countryCode"] == country_code


@pytest.mark.parametrize("phone_number,country_code", [
    ("2125690123", "ESP"),
    ("2125690123", "MEX"),
])
def test_get_information_valid_phone_number_with_country_code(client, phone_number, country_code):
    # test valid phone number with contry code
    response = client.get(
        base_url,
        params=f"phoneNumber={phone_number}&countryCode={country_code}"
    )

    assert response.status_code == 200
    assert response.json()["detail"]["error"] == {
        "countryCode": "required value is missing"
    }


def test_get_error_valid_phone_number_without_country_code(client):
    # test valid phone number without contry code
    response = client.get(
        base_url,
        params=f"phoneNumber=631%203118150"
    )

    assert response.status_code == 200
    assert response.json()["detail"]["error"] == {
        "countryCode": "required value is missing"
    }
