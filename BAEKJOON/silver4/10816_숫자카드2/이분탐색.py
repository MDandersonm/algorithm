def lower_bound(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


def upper_bound(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    # target 숫자의 시작 위치와 끝 위치를 찾는다.
    lower = lower_bound(cards, target)
    upper = upper_bound(cards, target)

    # 끝 위치 - 시작 위치를 하면 target 숫자의 개수가 나온다.
    print(upper - lower, end=' ')
