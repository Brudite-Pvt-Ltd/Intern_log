def merge_intervals(intervals):
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    result = []
    currentInterval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= currentInterval[1]:
            currentInterval[1] = max(currentInterval[1], interval[1])
        else:
            result.append(currentInterval)
            currentInterval = interval

    result.append(currentInterval)

    return result

intervals = [[1, 3], [2, 6], [4, 5], [8, 10], [5, 10], [20, 40], [30, 50]]
merged = merge_intervals(intervals)
print(merged)

