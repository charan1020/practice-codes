def repeat_marker(i):
    result = []
    for _ in range(i):
        result.append("marker")
    return result

# Example
if __name__ == "__main__":
    print(repeat_marker(3))  # ['marker', 'marker', 'marker']