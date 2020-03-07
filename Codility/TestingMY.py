def solution(A):
    # write your code in Python 3.6
    result = ""
    str_A = str(A)
    j = str_A.__len__() - 1
    for i in range(0, str_A.__len__()):
        if str_A.__len__() % 2 == 0 and i == int(str_A.__len__() / 2):
            break
        elif str_A.__len__() % 2 != 0 and i == int(str_A.__len__() / 2) + 1:
            break
        elif str_A.__len__() % 2 != 0 and i == int(str_A.__len__() / 2):
            result += str_A[i]
        else :
            result += str_A[i] + str_A[j - i]
    return result


A = 123456789123456
print(solution(A))

s = 'Hello'
print(s[0:-1])
