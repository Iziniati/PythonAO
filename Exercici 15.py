def gran(a, b):
    if a > b:
        return a
    else:
        return b

# Proves
print(gran(3, 7))     # 7
print(gran(10, 2))    # 10
print(gran(-5, -1))   # -1
print(gran(4, 4))     # 4 (són iguals, retorna un d’ells)

