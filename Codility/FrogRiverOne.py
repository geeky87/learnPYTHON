import array


def solution(X, A):
    counter = 1
    leaves = list()
    frog_step = 1
    for i in range(len(A)):
        if frog_step <= X:
            if frog_step == A[i]:
                counter += 1
                frog_step += 1
                try:
                    leaves.remove(A[i])
                except:
                    continue
            elif frog_step in leaves:
                counter += 1
                try:
                    leaves.remove(frog_step)
                    leaves.append(A[i])
                    frog_step += 1
                except:
                    frog_step += 1
                    leaves.append(A[i])
                    continue
            else:
                leaves.append(A[i])
    if frog_step <= X:
        for k in range(0, leaves.__len__()):
            if frog_step in leaves:
                counter += 1
                try:
                    leaves.remove(frog_step)
                    frog_step += 1
                except:
                    frog_step += 1
                    continue
    if frog_step < X:
        return -1
    else:
        return counter


z = array.array('i', [1, 3, 1, 4, 2, 3, 5, 4])
res1 = solution(5, z)
print(res1)
