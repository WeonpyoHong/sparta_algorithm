
# 알고리즘 더 풀어보기(2)
# 반복되지 않는 문자

#  풀이법 ===================================

input = "abacdabae"
input = "abadcabae"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    not_repeating_array = []

    # 일단 배열에 빈도수 저장
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    # 빈도수가 1인 것만 뽑아서 배열만들기
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_array.append(chr(index + ord('a')))

    # 다시 한번 돌려서, 빈도수 1인 것들과 비교
    for char in string:
        for alphabet in not_repeating_array:
            if char == alphabet:
                return char

    return '_'


result = find_not_repeating_character(input)
print(result)

