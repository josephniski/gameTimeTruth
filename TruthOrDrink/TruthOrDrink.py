import csv
import random
import math

class truthOrDrink():

    def __init__(self):
        self.row_count = 0 #number of rows in CSV
        self.row = [] #actual questions
        self.asked_questions = [] #questions that have been asked so far
        self.players = [] #attempting to have dynamically allocated list of lists
        '''
        For self.players, I want to have it loaded in each time with a name. 
        ie - player Joe is list 1. Then all questions with name Joe will be entered in this list
            The first element of this list will be the string 'joe' which differentiates the lists
        '''

    def populate(self): #populates the initial list of questions from csv (once)
        with open('stowe_truth_drink.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                #self.row.append("none")
                for rows in csv_reader:
                    if rows[0] not in (None, ''):
                        self.row_count += 1
                        self.row.append(rows)

    def printQuestion(self, name): #iterates over list of questions and prints random one
        name_row = []
        name_row_count = 0
        if name == '': #prints questions if able to be asked to anyone
            rand_row = random.randint(1, self.row_count - 1) #generates random number 
            print(self.row[rand_row][0]) #prints question at generated number 
            self.asked_questions.append(self.row[rand_row][0]) #adds asked question to list of asked questions 
            self.row.remove(self.row[rand_row]) #removes the question from list of all questions 
            self.row_count -= 1 #reduces the number of questions 
        else: #prints questions directed at specific people
            for rows in self.row:
                if name in rows[1]:
                    if rows[0] not in self.asked_questions:
                        name_row_count += 1
                        name_row.append(rows[0])
            rand_row = random.randint(1, name_row_count - 1)
            self.asked_questions.append(self.row[rand_row])
            print(name_row[rand_row])
            name_row.remove(name_row[rand_row])

    def checkPlayer(self, name):
        if name in self.row[0][1]:
            self.players.append(name)
            print("You added " + name + " to the game. Anyone else? (Y/N)")
        else:
            print("This game is not for that person")
            print("Would you like to add anyone else to the game? (Y/N)")
            
    def whoIsPlaying(self):
        print("Who is playing?")
        name = input().lower()
        self.checkPlayer(name)
        while True:                  
            continue_ = input().lower()
            if continue_ == 'n':
                break
            elif continue_ == 'y':
                print("Who else is playing?")
                name = input().lower()
                if name in self.players:
                    print("This player already exists, try again...")
                else:
                    self.checkPlayer(name)
            else:
                print("Please type Y or N to continue")
                                           

    def runGame(self):
        self.populate()
        self.whoIsPlaying()
        print("This is who is playing!")
        print(self.players)
        while(True):
            print("Who are you targeting?")
            name = input().lower()
            if name == 'no one':
                name = ''
            #if name in self.row[0][1]:
            if name in self.players:
                self.printQuestion(name)
            elif name == "done":
                print("Thank you for playing!")
                exit(0)
            else:
                print("This person does not exist, try again...")
            

game = truthOrDrink()
game.runGame()