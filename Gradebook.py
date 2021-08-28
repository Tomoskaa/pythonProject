# kreiram konstruktor prviot argument mi e sekogas self
class Student:

    def __init__(self, ime, ocena):
        self.ime = ime
        self.ocena = ocena

    # definiranje na krajna ocena na studentite
    def krajna_ocena(self):
        if self.ocena > 90 and self.ocena <= 100:
            return '10'
        elif self.ocena > 80 and self.ocena <= 90:
            return '9'
        elif self.ocena > 70 and self.ocena <= 80:
            return '8'
        elif self.ocena > 60 and self.ocena <= 70:
            return '7'
        elif self.ocena > 50 and self.ocena <= 60:
            return '6'
        else:
            return '5'

    # pecatenje
    def __str__(self):
        return "\t" + self.ime + ":" + " " + str(self.krajna_ocena())


if __name__ == '__main__':

    students = {}
    recnik_predmet = {}
    flag = 1

    while flag == 1:

        # vnesuvam podatoci se dodeka ne se vnesi 'end'
        podatoci = input()
        if podatoci == "end":
            break

        # podatocite kako sto gi vnesuvam gi odvojuvam pomegju sebe so split(",")
        line = podatoci.split(",")

        # python mi e skriptiracki jazik pa raboti linija po linija zatoa mozam vaka da gi pretstavam
        ime = line[0]
        prezime = line[1]
        index = line[2]
        predmet = line[3]
        teorija_poeni = line[4]
        prakticno_poeni = line[5]
        lab_poeni = line[6]

        students.update({index: ime + " " + prezime})

        # pravam proverka dali studentot e dodaden vo recnikot so studenti ama spored index
        # zato sto toa e edinstveno sto gi identifikuva(poslednite test primeri)
        # ima studenti so isto ime i prezime a razlicen index zato proverkata ja pram po index

        if index in recnik_predmet:
            vkupno_poeni = int(teorija_poeni) + int(prakticno_poeni) + int(lab_poeni)
            subject = Student(predmet, vkupno_poeni)
            recnik_predmet[index].append(subject)

        # ako go ima studentot i povtorno se javuva togas samo predmetot go dodavam
        else:
            vkupno_poeni = int(teorija_poeni) + int(prakticno_poeni) + int(lab_poeni)
            subject = Student(predmet, vkupno_poeni)
            recnik_predmet.update({index: [subject]})

    for student in recnik_predmet:
        print("Student: " + students[student])
        for student1 in recnik_predmet[student]:
            print(student1)
        print()