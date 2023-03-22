def solution(n):
    PF = []
    answer = []
    i = 2

    while i <= n:
        if n % i == 0:
            PF.append(i)
            n = n // i
        else:
            i+=1
    for j in PF:
        if j not in answer:
            answer.append(j)
    return answer

if __name__ == '__main__':
    print(solution(12))   
    print(solution(17))  
    print(solution(420))  