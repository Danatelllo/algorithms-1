def factory(kg, zag, det, det_now):
    if det > zag or zag > kg:
        return det_now
    if kg > 0:
        now_zag = kg // zag
        kg -= zag * now_zag
        for j in range(now_zag):
            det_now += zag // det
            kg += zag - (zag // det) * det
        if kg // zag > 0:
            return factory(kg, zag, det, det_now)
        else:
            return det_now


N, K, M = map(int, (input().split()))
detNow = 0
zagNow = 0
print(factory(N, K, M, detNow))