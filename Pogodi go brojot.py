

print("Zamislete broj")
zamislenBroj = int(input())

broj = None
while broj != zamislenBroj:
    print("Vnesete broj:")
    broj = int(input())
    print("Dali vashiot broj e ",broj,"?")
    if broj < zamislenBroj:
        print("Pogolem")
    elif broj > zamislenBroj:
        print("Pomal")
    else:
        print("Tocen")