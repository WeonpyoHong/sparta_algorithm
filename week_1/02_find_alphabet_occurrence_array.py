
# 최빈값 찾기 -2 (일반 최빈값을 배열로 반환하는 함수)

# 아스키코드의 개념을 알아야함

# 나의 풀이 방법

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():  # 빈칸을 걸러낼 필요
            alphabet_occurrence_array[ord(char) - ord('a')] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))



# 강사님 풀이 방법

def find_alphabet_occurrence_array2(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array2("hello my name is sparta"))


#ord('알파벳')  ===> 아스키코드로 변환