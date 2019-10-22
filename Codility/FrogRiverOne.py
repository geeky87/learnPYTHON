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
                except:
                    frog_step += 1
                    continue
            else:
                leaves.append(A[i])
        else:
            break
    return counter


z = array.array('i', [1, 3, 1, 4, 2, 3, 5, 4])
res1 = solution(5, z)
print(res1)
