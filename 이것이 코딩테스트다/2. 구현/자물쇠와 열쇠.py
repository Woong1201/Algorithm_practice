def rotate_key(key):
    new_key = []
    for j in range(len(key[0])):
        part = []
        for i in range(len(key)-1, -1, -1):
            part.append(key[i][j])
        new_key.append(part)
    return new_key

def unlock(key, lock, hole):
    for i in range(len(key)+len(lock)-1):
        for j in range(len(key[0])+len(lock[0])-1):
            ok = 0
            differ = 0
            range_row = [max(0,i-len(key)+1), min(len(lock),i+1)]
            range_col = [max(0,j-len(key[0])+1), min(len(lock[0]),j+1)]
            start = [i-len(key)+1,j-len(key[0])+1]
            for row in range(range_row[0],range_row[1]):
                for col in range(range_col[0],range_col[1]):
                    if lock[row][col] == key[row-start[0]][col-start[1]]:
                        differ = 1
                        break
                    elif lock[row][col] == 0:
                        ok += 1
                if differ == 1:
                    break
            if differ == 0 and ok == hole:
                return True
    return False

def solution(key, lock):
    hole = len(lock)*len(lock[0])-sum(sum(i) for i in lock)
    for i in range(4):
        if unlock(key, lock, hole) == True:
            return True
        key = rotate_key(key)
    return False

key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))