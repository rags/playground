def sum_to_target(arr, target,  combs = [[]]):
    if not arr: return combs if target == 0 else []
    last,  new_arr = arr[-1], arr[:-1]
    if target >= last:
        return sum_to_target(new_arr, target - last, map(lambda comb: comb + [last], combs)) + sum_to_target(new_arr, target, combs)

    return sum_to_target(new_arr, target, combs)


print(sum_to_target([1, 3, 5, 7, 9], 15)) #[[9, 5, 1], [7, 5, 3]]
print(sum_to_target([1, 3, 5, 7, 9], 26)) #[]
print(sum_to_target([1, 5, 5, 3, 9], 10, [[]])) #[[9, 1], [5, 5]]
