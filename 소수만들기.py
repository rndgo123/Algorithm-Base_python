문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12977

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(nums):
    n = len(nums)
    answer = []
    
    def is_prime(x) : 
        if x < 2 :
            return False
        for i in range(2, x-1) :
            if x % i == 0 :
                return False
        return True
    
    for i in range(n) :
        for j in range(i+1, n) :
            for m in range(j+1, n) :
                x = nums[i] + nums[j] + nums[m]
                if is_prime(x) == True :
                    answer.append(x)
    return len(answer)
