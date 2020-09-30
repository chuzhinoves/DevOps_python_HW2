sentence = input("Enter sentece: ").split(" ")
[print(ind + 1, word if len(word) < 10 else word[:10]) 
 for ind, word in enumerate(sentence)]
