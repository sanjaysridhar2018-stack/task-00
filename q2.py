def process_list(n):
    copy = n.copy()

    for i in list(copy):
        if i < 0:
            copy.remove(i)

    copy.append(0)
    copy.sort()

    return copy


og = [5, -2, 8, -1, 3]
res = process_list(og)

print("Original:", og)
print("Result:", res)
