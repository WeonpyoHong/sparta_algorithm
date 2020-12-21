
# 알고리즘 더 풀어보기(2)
# 반복되지 않는 문자

# 강사님 풀이법 ===================================

input = "abacabade"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    # 반복되지 않는 문자 담기
    not_repeating_character_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    # 가장먼저 나오는 char값 반환하기
    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"

result = find_not_repeating_character(input)
print(result) # -> d