

def proverka(x):
    if x % 2 == 0:
        return 'Paren'
    else:
        return 'Neparen'

def deliv(x):
    if x % 4 == 0:
        return 'Deliv so 4'
    else:
        return 'Ne e deliv so 4'

print("Vnesete broj:")
broj = int(input())

print(proverka(broj))
print(deliv(broj))
