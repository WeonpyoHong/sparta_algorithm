
# 문자열 뒤집기

input = "01111011"
# input = "1101101100"

# 0 -> 1  또는  1 -> 0 (변할때 뒤집어야 함)

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    start_num = string[0]
    current_num = string[0]
    number_of_change = 0

    for char in string:
        if current_num == char:
            current_num = char
            continue
        else:
            if start_num != char:
                number_of_change += 1
            current_num = char

    return number_of_change


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)