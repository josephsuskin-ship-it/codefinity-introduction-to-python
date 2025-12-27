# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

is_raw = "raw" in description

contains_raw = is_raw

is_Imported = "Imported" in description

contains_Imported = is_Imported

correct_price_type = type(price) == float

price_is_float = correct_price_type

correct_quantity_type = type(count) == int

count_is_int = correct_quantity_type

print("Contains 'raw':" , contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)

