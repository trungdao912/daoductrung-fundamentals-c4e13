def is_inside(a, b):
    if a[0] in range(b[0], b[0] + b[2]) and a[1] in range(b[1] + b[3]):
        return True
    else:
        return False
   

print(is_inside([100, 120],[140, 60, 100, 200]))

