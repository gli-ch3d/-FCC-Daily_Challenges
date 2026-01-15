## Sorted Array?
# 2026-01-08

def is_sorted(arr):
    trend = "null"
    prev = arr.pop(0)
    for i in arr:
        current = i
        if (current > prev) and (trend == "null" or trend == "Ascending"):
            trend = "Ascending"
        elif (current < prev) and (trend == "null" or trend == "Descending"):
            trend = "Descending"
        else:
            trend = "Not sorted"
            break
        prev = i
    return trend