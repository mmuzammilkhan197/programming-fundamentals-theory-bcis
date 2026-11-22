for i in range(1, 31):
    if i == 25:
        break          # stop the loop at 25
    if i == 10:
        pass           # does nothing, just a placeholder
    if i % 3 == 0:
        continue       # skip numbers divisible by 3
    print(i, end=" ")