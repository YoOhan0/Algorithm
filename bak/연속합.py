import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numlist = list(map(int, input().split()))
current_sum = numlist[0]
max_sum = numlist[0]

# 각각의 i단계에서는, i까지의 요소를 고려 했을 때, 연속된 부분 수열의 최대 값을 구한다.
for i in range(1,n):# i 요소까지 고려 했을 때의 최대 값은, i를 포함하는 최대 값도 고려해야 하지만, i를 포함하지 않는 최대 값도 고려해야 한다.
    
    current_sum = max(numlist[i], current_sum + numlist[i]) # i를 포함하는 부분 수열을 고려.
    max_sum=max(max_sum, current_sum) # i를 포함하지 않는 부분 수열을 고려.(max_sum이 의미하는 바를 생각 해보면, 이전 i-1단계까지 모든 경우의 수를 고려 했을 때의 최대 값이다.)

print(str(max_sum))