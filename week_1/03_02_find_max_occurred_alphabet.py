
# 알파벳의 최빈값 찾기 방법 - 2

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    # 빈도수 저장
    max_occurrence = 0
    # 가장 많이 나왔던 알파벳의 인덱스 저장
    max_alphabet_index = 0

    # [4,0,0,.....]
    # 이 형태의 배열에서 인덱스 꺼내기
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    # 인덱스 가지고 ===> 아스키코드 ===> 알파벳으로 변환
    alphabet_asci_code = max_alphabet_index + ord('a')
    return_alphabet = char(alphabet_asci_code)

    return return_alphabet       # char(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)


# python char to ascii code
# a -> 0
# a -> ord('a') -> 97 - ord('a') = 0

# python number to char
# 0 -> a
# 0 -> 0 + ord('a') -> 97 -> chr(97) -> a
