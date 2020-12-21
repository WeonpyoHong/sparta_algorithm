genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 1.속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 2.장르 내에서 많이 재생된 노래를 먼저 수록한다.(두곡씩 수록)
# 3.장르 내에서 재생 횟수가 같다면 고유 번호가 낮은 노래 먼저 수록한다.

# 장르 별로(key) 우선 재생된 횟수(Value)를 저장해야 해야함
# 장르 별로 곡의 정보(인덱스, 재생횟수) 배열로 묶어 저장

def get_melon_best_album(genre_array, play_array):
    music = []
    sum = []
    genre_index = 0
    play_index = 0
    result = []

    for i in range(len(genre_array)):
        if genre_array[i] not in music:
            music.append(genre_array[i])
            sum.append(play_array[i])
        else:
            for j in range(len(music)):
                if music[j] == genre_array[i]:
                    sum[j] = sum[j] + play_array[i]

            # sum[i] += sum[i] + play_array[i]
    print(music, sum)

    music.sort()
    sum.sort()








    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!



# a = {"fast": 33, "slow": 22}
# a.items()
# [('fast',33), ('slow', 22)]

# a.items()       # 그 아이템 중에 item[1]을 기준으로 정렬할꺼야

# sorted(a.items(), key=lambda item: item[1])
# 배열, key라는 람다함수(특정 인자를 받아서, 어떤 값으로 돌려줄 것인지를 간단한 수식으로 표현)

# [('slow', 22), ('fast',33)]

#내림차순 정렬
# sorted(a.items(), key=lambda item: item[1], reverse=True)
# [('fast',33), ('slow', 22)]