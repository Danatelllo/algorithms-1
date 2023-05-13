counter1 = int(input())
counter2 = int(input())
train1 = int(input())
train2 = int(input())
wait_any_tr1 = train1 + counter1 * (train1 - 1)
wait_all_tr1 = train1 + counter1 * (train1 + 1)
wait_any_tr2 = train2 + counter2 * (train2 - 1)
wait_all_tr2 = train2 + counter2 * (train2 + 1)
min_max = min(wait_all_tr2, wait_all_tr1)
max_min = max(wait_any_tr2, wait_any_tr1)
if min_max >= max_min:
    print(max_min, min_max)
else:
    print(-1)
