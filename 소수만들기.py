def solution(nums):
    n = len(nums) #range 지정
    answer = []
    
    def is_prime(x) : #소수 확인 함수
        if x < 2 :
            return False
        for i in range(2, x-1) :
            if x % i == 0 :
                return False
        return True
    
    for i in range(n) : 
        for j in range(i+1, n) :
            for m in range(j+1, n) :
                x = nums[i] + nums[j] + nums[m] #범위를 한 개씩 올려 조합 3개의 숫자 합산 생성
                if is_prime(x) == True : 
                    answer.append(x)
    return len(answer)
