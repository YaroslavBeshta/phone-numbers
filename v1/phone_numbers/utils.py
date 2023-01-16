from v1.phone_numbers.dial_code_mappings import DIAL_TO_COUNTRY


def split_phone_into_codes(phone_number: str) -> tuple:
    phone_number = phone_number.replace(" ", "")
    if phone_number.startswith("+"):
        phone_number = phone_number[1:]

    # iterate first 3 digits to properly split phone number into
    # country code, area code, and local phone number
    # 12125690123 =>
    # 1 - country code
    # 212 - area code
    # 5690123 - local phone number
    country_code_len = 1
    for i in range(4):
        country_dial = phone_number[:i + 1]
        country_code = DIAL_TO_COUNTRY.get(f"+{country_dial}")
        if country_code:
            country_code_len += i
            area_code = phone_number[country_code_len:country_code_len + 3]
            local_phone_number = phone_number[country_code_len + 3:]

            # check if length of local phone number is in range to find most suitable country code
            # check if length of country code, local phone number and area code in range of 9 to 15
            if (6 <= len(local_phone_number) <= 8
                    and 9 <= country_code_len + len(local_phone_number) + 3 < 15):
                break
    
    if country_code is None:
        return (None, None, phone_number[:3], phone_number[3:])
    
    return (country_code, f"+{country_dial}", area_code, local_phone_number)
