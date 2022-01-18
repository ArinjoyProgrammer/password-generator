import random



class PaswordGen:
    def passGenWork():
        letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3' ,'4', '5', '6', '7', '8', '9', '0']

        letterRandom1 = random.choice(letterList)
        letterRandom2 = random.choice(letterList)
        letterRandom3 = random.choice(letterList)
        letterRandom4 = random.choice(letterList)
        letterRandom5 = random.choice(letterList)
        letterRandom6 = random.choice(letterList)
        letterRandom7 = random.choice(letterList)
        letterRandom8 = random.choice(letterList)
        letterRandom9 = random.choice(letterList)
        letterRandom10 = random.choice(letterList)


        d1 = letterRandom1
        d2 = letterRandom2
        d3 = letterRandom3
        d4 = letterRandom4
        d5 = letterRandom5
        d6 = letterRandom6
        d7 = letterRandom7
        d8 = letterRandom8
        d9 = letterRandom9
        d10 = letterRandom10

        password = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
        
        for items in password:
            print(items, end='')
    
    passGenWork()
