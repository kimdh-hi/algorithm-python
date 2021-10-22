genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    result = []
    dict = {}
    dict_detail = {}
    for i in range(len(genre_array)):
        if genre_array[i] not in dict:
            dict[genre_array[i]] = play_array[i]
            dict_detail[genre_array[i]] = [[i, play_array[i]]]
        else:
            dict[genre_array[i]] += play_array[i]
            dict_detail[genre_array[i]].append([i, play_array[i]])

    dict_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in dict_items:
        idx_play_list = dict_detail[k]
        idx_play_list = sorted(idx_play_list, key = lambda x: x[1], reverse=True)
        for i in range(len(idx_play_list)):
            if i > 1:
                break
            result.append(idx_play_list[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!


