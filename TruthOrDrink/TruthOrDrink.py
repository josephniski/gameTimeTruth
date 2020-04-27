import csv
import random
import math

class truthOrDrink():

    def __init__(self):
        self.row_count = 0
        self.row = []
        self.asked_questions = []

    def populate(self):
        with open('stowe_truth_drink.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for rows in csv_reader:
                    if rows[0] not in (None, ''):
                        self.row_count += 1
                        self.row.append(rows)

    def printQuestion(self, name):
        name_row = []
        name_row_count = 0
        if name == '':
            rand_row = random.randint(1, self.row_count - 1)
            print(self.row[rand_row][0])
            self.asked_questions.append(self.row[rand_row][0])
            self.row.remove(self.row[rand_row])
            self.row_count -= 1
        else:
            for rows in self.row:
                if name in rows[1]:
                    if rows[0] not in self.asked_questions:
                        name_row_count += 1
                        name_row.append(rows[0])
            rand_row = random.randint(1, name_row_count - 1)
            self.asked_questions.append(self.row[rand_row])
            print(name_row[rand_row])
            name_row.remove(name_row[rand_row])

    def runGame(self):
        self.populate()
        print("This is who is playing!")
        print(self.row[0][1])
        while(True):
            print("Who are you targeting?")
            name = input().lower()
            if name == 'no one':
                name = ''
            if name in self.row[0][1]:
                self.printQuestion(name)
            else:
                print("This person does not exist, try again...")
                self.runGame()
            

game = truthOrDrink()
game.runGame()