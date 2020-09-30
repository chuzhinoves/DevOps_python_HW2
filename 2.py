#уверен, что есть способ короче, но в голову не пришел
input_array_str = input("введите список разделенный пробелами: ").split(" ")
if len(input_array_str) > 0:
    for i in range(1, len(input_array_str), 2):
        a = input_array_str[i] 
        input_array_str[i] = input_array_str[i-1]
        input_array_str[i-1] = a
print(input_array_str)
