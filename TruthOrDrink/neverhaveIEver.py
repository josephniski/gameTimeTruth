
import csv
import random
import math

class neverHaveIEver():

    def __init__(self):
        self.row_count = 0 #number of rows in CSV
        self.row = [] #actual questions
        self.asked_questions = [] #questions that have been asked so far
        self.players_questions = [] #attempting to have dynamically allocated list of lists
        self.players_list = [] #list of people playing in given game

    def populate(self): #populates the initial list of questions from csv (once)
        with open('stowe_never.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for rows in csv_reader:
                    if rows[0] not in (None, ''):
                        self.row_count += 1
                        self.row.append(rows)

    def printQuestion(self):
        rand_row = random.randint(1, self.row_count - 1) #generates random number 
        print(self.row[rand_row][0]) #prints question at generated number 
        self.asked_questions.append(self.row[rand_row]) #adds asked question to list of asked questions 
        self.row.remove(self.row[rand_row]) #removes the question from list of all questions 
        self.row_count -= 1 #reduces the number of questions 

    def runGame(self):
        print("Welcome to Never Have I Ever") #Intro to the game 
        self.populate() #populating the local list of questions
        while(True):
            print("Do you want a question?")
            name = input().lower()
            if name[0].lower == 'y':
                self.printQuestion()
            elif name == "done":
                print("Thank you for playing!")
                exit(0)
            

game = neverHaveIEver()
game.runGame()