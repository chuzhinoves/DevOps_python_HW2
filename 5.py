reiting = [7, 5, 5, 2, 1]
new_element = int(input("введите новый элемент: "))
for ind, element in enumerate(reiting):
    if new_element >= element:
        ind = ind - 1
        break
reiting.insert(ind + 1, new_element)
print(reiting)
