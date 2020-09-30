# в уловии ничего не сказано и я понял проверку так
array_diff_type = [2, 'r', 3.4, (1,3), ["d", "f"], {"d":2, "s":3}, set([1,2,3]), 1]
type_array = [type(i) for i in array_diff_type]
print(type_array)
correct_type = [int, str, float, tuple, list, dict, set, type]
[print (f"элемент {i} не соответсвтует нужному типу {correct_type[i]}")
 for i in range(len(array_diff_type)) if correct_type[i] != type_array[i]]
