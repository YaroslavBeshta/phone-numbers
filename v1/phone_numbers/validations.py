import re


def is_valid_phone_number(phone_number: str) -> bool:
    """Validate phone number. 

    Phone number might contain optional spaces and +:
    1 212 5690123 => True
    +12125690123 => True
    +52 631 3118150 => True

    1-212-569-0123 => False
    +1-212-569-0123 => False
    """
    pattern = re.compile(r'^(\+?\d{1,3})?\s?\d{3}\s?\d{6,8}$')
    return pattern.match(phone_number) is not None
