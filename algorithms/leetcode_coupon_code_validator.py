import re


def validate_coupons(code: list[str], business_line: list[str], is_active: list[bool]) -> list[str]:
    def is_valid_code(code: str) -> bool:
        if code == "":
            return False
        pattern = r"[a-zA-Z0-9_]+"
        return re.fullmatch(pattern, code)

    def is_valid_business_line(business_line: str) -> bool:
        return business_line in ("electronics", "grocery", "pharmacy", "restaurant")

    coupons = []
    for i in range(len(code)):
        if is_valid_code(code[i]) and is_valid_business_line(business_line[i]) and is_active[i]:
            coupons.append([business_line[i], code[i]])
    coupons.sort()

    result = []
    for coupon in coupons:
        result.append(coupon[1])

    return result


print(validate_coupons(["SAVE20", "", "PHARMA5", "SAVE@20"], ["restaurant", "grocery", "pharmacy", "restaurant"],
                       [True, True, True, True]))
print(validate_coupons(["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"], ["grocery", "electronics", "invalid"],
                       [False, True, True]))
print(validate_coupons(["1OFw", "0MvB"], ["electronics", "pharmacy"], [True, True]))
