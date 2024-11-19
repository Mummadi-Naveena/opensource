T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    score_per_test_case = X // 10  
    score = score_per_test_case * N
    print(score)
