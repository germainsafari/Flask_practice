def alphabetic_order(arr):
    result = []
    for word in arr:
        for i in range(len(word)):
            if ord(word[i]) < ord(word[0]):
                result.append("Yes")
                break
        else:
            result.append("No")
    return result



names = ["Germain", "safari", "age"]
result = alphabetic_order(names)
print(result)