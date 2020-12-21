input = "abcabcabcabcdededededede"


"aabbaccc"	# -> 7
"ababcdcdababcdcd"	# -> 9
"abcabcdede"	# -> 8
"abcabcabcabcdededededede"	# -> 14
"xababcdcdababcdcd"	# -> 17



def string_compression(string):
    n = len(string)
    compression_length_array = []
    for split_size in range(1, n // 2 + 1):
        # splited = []
        # for i in range(0, n, split_size):
        #     splited.append(string[i:i + split_size])
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        print(splited)
        compressed = ""
        count = 1     # 이전값과 자기값을 비교한 것이기 때문에...

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:  #
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1   # 반복이 끝났으니까 초기화

        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        print(compressed)
        compression_length_array.append(len(compressed))

    return min(compression_length_array)    #배열에서 최소값을 반환


print(string_compression(input))  # 14 가 출력되어야 합니다!