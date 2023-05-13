from collections import deque
first_player = deque(map(int, input().split()))
second_player = deque(map(int, input().split()))
counter = 0
while len(second_player) > 0 and len(first_player) > 0 and counter < 10 ** 6:
    condition = first_player[0] != 9 and second_player[0] != 0
    condition2 = first_player[0] == 0 and second_player[0] == 9
    condition3 = first_player[0] == 9 and second_player[0] != 0
    condition4 = first_player[0] != 9 and second_player[0] == 0
    condition_win = condition2 or condition3 or condition4
    if (first_player[0] > second_player[0] and condition) or condition_win:
        a = second_player.popleft()
        b = first_player.popleft()
        first_player.append(b)
        first_player.append(a)
    else:
        a = second_player.popleft()
        b = first_player.popleft()
        second_player.append(b)
        second_player.append(a)
    counter += 1
if len(second_player) > 0:
    print('second', counter)
elif len(first_player) > 0:
    print('first', counter)
else:
    print("botva")