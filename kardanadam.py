import turtle
import csv
import random


def main():
    turtle.bgpic("C:\\Users\\Hessam\\Desktop\\pythonProject3\\snowmanTree.gif")

    print("Kardan Adam Oyunu Basladi")
    print("--------------------------")

    file = open("C:\\Users\\Hessam\\Desktop\\pythonProject3\\cities.txt", "r")
    satir = csv.reader(file)

    cities = [c for c in satir]
    selection = random.choice(cities)
    city = (''.join(selection)).lower()
    print(len(city), "harfli bir sehir ismi?")
    soru = ""

    for _ in city:
        soru += "_ "

    print(soru)
    print(city)

    deneme = 7
    tahmin = []

    while deneme > 0:
        letter = input("Bir harf tahmin ediniz : ")
        sonuc = ""
        chk = 0
        chc = 0
        ctrl = 0

        if len(tahmin) != 0:
            if letter not in tahmin:
                tahmin.append(letter)
                chc = 1
            if chc == 0:
                print("Bu harfi daha once girdiniz. Yeniden deneyin.")
                continue

            for s in city:
                if letter == s:
                    chk = 1

            if chk == 0:
                print("Maalesef", letter, "harfinden hic yok.")
                ciz(deneme)
                deneme -= 1
                if deneme == 0:
                    print("Bilemediniz. Sehir: ", city)
                    break
                else:
                    continue

            for a in city:
                if a in tahmin:
                    sonuc += a + " "
                    ctrl += 1
                else:
                    sonuc += "_ "

            print(sonuc)

            if ctrl == len(city):
                print("...Bildiniz....")
                break

        else:
            tahmin.append(letter)
            for s in city:
                if letter == s:
                    chk = 1
            if chk == 0:
                print("Maalesef", letter, "harfinden hic yok.")
                ciz(deneme)
                deneme -= 1
                continue

            for s in city:
                if s in tahmin:
                    sonuc += s + " "
                    ctrl += 1
                else:
                    sonuc += "_ "

            print(sonuc)


def ciz(d):

    if d == 7:
        turtle.speed(10000)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.pensize(15)
        turtle.color("black")
        turtle.circle(5)
        turtle.penup()
    elif d == 6:
        turtle.forward(48)
        turtle.pendown()
        turtle.circle(5)
        turtle.penup()
    elif d == 5:
        turtle.right(90)
        turtle.forward(18)
        turtle.right(90)
        turtle.forward(23)
        turtle.pendown()
        turtle.pensize(11)
        turtle.color("orange")
        turtle.circle(12)
        turtle.penup()
    elif d == 4:
        turtle.forward(33)
        turtle.left(90)
        turtle.forward(23)
        turtle.pendown()
        turtle.color("red")
        turtle.circle(30, 180)
        turtle.penup()
    elif d == 3:
        turtle.left(180)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(22)
        turtle.pendown()
        turtle.pensize(10)
        turtle.color("black")
        turtle.circle(7)
        turtle.penup()
        turtle.left(90)
        turtle.forward(50)
        turtle.pendown()
        turtle.pensize(10)
        turtle.circle(7)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.pensize(10)
        turtle.circle(7)
    elif d == 2:
        turtle.penup()
        turtle.left(90)
        turtle.forward(92)
        turtle.left(90)
        turtle.forward(80)
        turtle.right(45)
        turtle.pensize(13)
        turtle.pendown()
        turtle.color("brown")
        turtle.forward(150)
    elif d == 1:
        turtle.penup()
        turtle.left(180)
        turtle.forward(150)
        turtle.right(45)
        turtle.forward(178)
        turtle.right(45)
        turtle.pendown()
        turtle.forward(150)


if __name__ == "__main__":
    main()
