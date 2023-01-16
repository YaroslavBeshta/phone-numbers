from typing import Optional

from fastapi import APIRouter, HTTPException

from v1.phone_numbers.dial_code_mappings import COUNTRY_TO_DEAL
from v1.phone_numbers.utils import split_phone_into_codes
from v1.phone_numbers.validations import is_valid_phone_number

router = APIRouter()


@router.get(
    "/phone-numbers",
    summary="Return phone number information",
    description=(
        "Endpoint that takes request"
        "parameters and returns information about a phone number."
    ),
    status_code=200
)
async def get_information_about_phone_number(phoneNumber: str, countryCode: Optional[str] = None):
    print(phoneNumber)
    if not is_valid_phone_number(phoneNumber):
        return HTTPException(
            status_code=422,
            detail={
                "phoneNumber": phoneNumber,
                "error": {
                    "phoneNumber": (
                        "phone number does not match E.164 format: "
                        "[+][country code][area code][local phone number]"
                    )
                }
            }
        )

    # divide phone number into 3 separate parts
    country_code, country_dial, area_code, local_phone_number = split_phone_into_codes(
        phoneNumber)

    if not country_code and not countryCode:
        return HTTPException(
            status_code=422,
            detail={
                "phoneNumber": phoneNumber,
                "error": {
                    "countryCode": "required value is missing"
                }
            }
        )

    if country_dial is None:
        country_dial_from_code = COUNTRY_TO_DEAL.get(countryCode)
        if country_dial_from_code is None:
            return HTTPException(
                status_code=422,
                detail={
                    "phoneNumber": phoneNumber,
                    "error": {
                        "countryCode": "required value is missing"
                    }
                }
            )
        country_dial = country_dial_from_code

    response = {
        "phoneNumber": f"{country_dial}{area_code}{local_phone_number}",
        "countryCode": country_code if country_code else countryCode.upper(),
        "areaCode": area_code,
        "localPhoneNumber": local_phone_number
    }

    return response
