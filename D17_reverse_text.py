def reverse_text(string):
    i=len(string)-1
    while i >= 0:
        yield string[i]
        i -= 1


for c in reverse_text("step"):
    print(c, end='')
