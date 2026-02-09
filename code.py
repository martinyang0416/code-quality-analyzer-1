def process(arr):
    while True:
        if not arr:
            break
        runs = []
        current = arr[0]
        count = 1
        for num in arr[1:]:
            if num == current:
                count += 1
            else:
                runs.append((current, count))
                current = num
                count = 1
        runs.append((current, count))
        to_remove = [i for i, (c, cnt) in enumerate(runs) if cnt >= 3]
        if not to_remove:
            break
        