
def invert_dict(d):
    inverse = dict()
    for key in d:
        # Ensure values is always a list
        values = d[key] if isinstance(d[key], list) else [d[key]]

        # Now process all values the same way
        for val in values:
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
    return inverse


def read_file_safely(filename):
    try:
        fin = open(filename, 'r')
        content = fin.read()
        local_vars = {}
        exec(content, {}, local_vars)
        fruits_dict = local_vars['fruits']
        result = invert_dict(fruits_dict)
        fin.close()
        return result
    except FileNotFoundError as e:
        print(f"Error: The file '{filename}' does not exist.")
        print("Technical details:", e)
        return None


result = read_file_safely('Unit8_input.py')
with open("Unit8_output.py", "w") as f:
    f.write(f"inverted_fruits = {result}\n")