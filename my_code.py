import pytest

def fix_phone_num(phone_num_to_fix):
    # Remove all non-digit characters
    phone_num_to_fix = ''.join(filter(str.isdigit, phone_num_to_fix))

    # Check if it's all digits and exactly 10 digits long
    if not phone_num_to_fix.isdigit():
        raise ValueError("Phone number must contain only digits.")
    if len(phone_num_to_fix) != 10:
        raise ValueError("Phone number must be exactly 10 digits long.")

    # Split into parts and reformat
    area_code = phone_num_to_fix[0:3]      # 512
    three_part = phone_num_to_fix[3:6]     # 555
    four_part = phone_num_to_fix[6:]       # 8823

    fixed_num = f"({area_code}) {three_part} {four_part}"
    return fixed_num

# Base test with clean inputs
def test_fix_phone_num():
    assert fix_phone_num("5125558823") == "(512) 555 8823"
    assert fix_phone_num("5554429876") == "(555) 442 9876"
    assert fix_phone_num("3216543333") == "(321) 654 3333"

# Tests with symbols and formatting (which should now pass)
def test_fix_phone_num_with_symbols():
    assert fix_phone_num("555-442-9876") == "(555) 442 9876"
    assert fix_phone_num("(321) 654 3333") == "(321) 654 3333"

