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
