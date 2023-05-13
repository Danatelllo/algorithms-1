t_room, t_cond = map(int, input().split())
variable = input()
if variable == 'freeze':
    if not t_room <= t_cond:
        print(t_cond)
    else:
        print(t_room)
if variable == 'heat':
    if not t_room >= t_cond:
        print(t_cond)
    else:
        print(t_room)
if variable == 'auto':
    print(t_cond)
if variable == 'fan':
    print(t_room)
