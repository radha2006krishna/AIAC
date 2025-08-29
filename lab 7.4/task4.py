def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            ratio = values[i] / (values[j] - values[i])
            results.append((i, j, ratio))
    return results
# Correction: Avoid division by zero and only compute ratio when denominator is not zero
def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            denominator = values[j] - values[i]
            if denominator != 0:
                ratio = values[i] / denominator
                results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
