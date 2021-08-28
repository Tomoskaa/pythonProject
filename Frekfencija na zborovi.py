

def frekfencija(string):
    string = string.split()
    zborovi = []

    for i in string:
        if i not in zborovi:
            zborovi.append(i)

    zborovi.sort()
    for i in range(0, len(zborovi)):
        print(zborovi[i],':',string.count(zborovi[i]))

if __name__ == '__main__':
    print("Vnesete string:")
    string = input()
    frekfencija(string)

