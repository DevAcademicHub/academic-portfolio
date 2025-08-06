names = ['Student1', 'Student2', 'Student3']
scores = [85, 92, 78]

# without using zip
for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")

# using zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# without using enumerate
for i in range(len(names)):
    print(f"{i}: {names[i]}")

# using enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")

# using items
scores_dict = dict(zip(names, scores))
print(scores_dict)
print(list(scores_dict.items()))

# for name, score in scores_dict.items():
#     print(f"{name}: {score}")