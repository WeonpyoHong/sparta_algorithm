all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 딕셔너리로 체크하는 방법
# 일단 모든 학생을 딕셔너리에 넣고, 현재 학생을 돌면서, 있는 학생은 제거,
# 마지막까지 키가 없어지지 않는 학생은 출석하지 않은 것



def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:   # O(N)
        student_dict[key] = True     #공간복잡도도 O(N) 만큼 걸림

    for key in present_array:   # O(N)
        del student_dict[key]   #제거

    for key in student_dict.keys():
        return key

# 배열은 처음부터 끝까지 탐색을 하지만, 딕셔너리는 아님


print(get_absent_student(all_students, present_students))





# 쉽게 구현할 수 있는 방법 =================================
# 시간 복잡도가 O(N^2)만큼 걸림
# for all_student in all_students:
#     for present_student in present_students:
#         if all_student == present_student:
#             break
#     else:
#         present_student
