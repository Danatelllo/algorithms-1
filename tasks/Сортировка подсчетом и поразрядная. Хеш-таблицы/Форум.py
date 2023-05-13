messages = dict()
topics = dict()
n = int(input())
for j in range(1, n + 1):
    number = int(input())
    if number == 0:
        topic = input()
        input()
        if topic not in topics:
            topics[topic] = 1
        else:
            topics[topic] += 1
        messages[j] = topic
    else:
        topics[messages[number]] += 1
        messages[j] = messages[number]
        input()
popular_topic = ''
maxim = 0
for j in topics:
    if topics[j] > maxim:
        maxim = topics[j]
        popular_topic = j
print(popular_topic)