def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

if __name__ == '__main__':
    print(solution("10","11"))   
    print(solution("1001","1111"))  