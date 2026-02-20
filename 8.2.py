data = [(1, 3), (3, 2), (2, 5), (5, 1)]
new_tup= sorted(data, key=lambda x: x[-1])
print(f"Sorted list : {new_tup}")
