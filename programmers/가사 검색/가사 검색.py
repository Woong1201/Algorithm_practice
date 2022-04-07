from bisect import bisect, bisect_left, bisect_right

def solution(words, queries):
    word_dic = {}
    answer = []

    for word in words:
        if len(word) not in word_dic:
            word_dic[len(word)] = [[word], [word[::-1]]]
        else:        
            word_dic[len(word)][0].append(word)
            word_dic[len(word)][1].append(word[::-1])

    for word_len in word_dic:
        word_dic[word_len][0].sort()
        word_dic[word_len][1].sort()

    for query in queries:
        len_query = len(query)
        if len_query not in word_dic:
            answer.append(0)
            continue
        if query[0] == query[-1] == '?':
            answer.append(len(word_dic[len_query][0]))
        elif query[0] == '?':
            idx = bisect_right(query, '?')
            query = query[:idx-1:-1]
            answer.append(bisect_right(word_dic[len_query][1],query+'~')-bisect_left(word_dic[len_query][1],query))
        else:
            idx = bisect_right(query[::-1], '?')
            query = query[:-idx]
            answer.append(bisect_right(word_dic[len_query][0],query+'~')-bisect_left(word_dic[len_query][0],query))
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))