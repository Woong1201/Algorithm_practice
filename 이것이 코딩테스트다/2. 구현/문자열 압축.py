def solution(string):
    length = len(string)
    answer = length

    for i in range(1, length//2 + 1):
        index = i
        s1 = string[:i]
        count = 1
        new_str = ''
        
        while index <= length:
            s2 = string[index:index+i]
            if s1 == s2:
                count += 1
            else:
                if count >= 2:
                    new_str += str(count)
                new_str += str(s1)
                count = 1
            index += i
            s1 = s2
        
        if index - i < length:
            new_str += string[index-i:]
        answer = min(answer, len(new_str))    
    return answer

s = 'aabbaccc'
print(solution(s))