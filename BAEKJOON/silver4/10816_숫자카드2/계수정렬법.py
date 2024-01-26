MAX_NUM = 10000000
OFFSET = 10000000

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 계수 정렬을 위한 배열 초기화
count = [0] * (2 * MAX_NUM + 1)

# 카드에 적힌 숫자들을 계수 정렬 배열에 기록
for card in cards:
    count[card + OFFSET] += 1

# 타겟 숫자들에 대해서 계수 정렬 배열에서 해당 숫자의 개수를 출력
for target in targets:
    print(count[target + OFFSET], end=' ')
