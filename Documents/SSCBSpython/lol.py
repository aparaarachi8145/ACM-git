def print_pattern():
    # First part of the pattern
    for i in range(1, 7):
        print('* ' * i)
    
    # Second part of the pattern
    for i in range(6, 0, -1):
        print('* ' * i)

print_pattern()
