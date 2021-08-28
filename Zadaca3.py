

def deliv(x, y):
    if x % y == 0:
        return 'Deliv'
    else:
        return 'Ne e deliv'

print("Vnesete dva broja:")
x = int(input())
y = int(input())

print(deliv(x, y))

