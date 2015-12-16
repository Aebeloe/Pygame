'''
Created on 07/12/2015

@author: Mads
'''
class Highscores():
    def __init__(self):
        self.scoreboard = []
        try:
            with open('highscores.txt', 'r') as f:
                for line in f:
                    self.scoreboard.append(line.rstrip())
        except Exception as e:
            pass

    def new_score(self, score):
        self.scoreboard.append(str(score))

    def save_score(self):
        with open('highscores.txt', 'w+') as f:
            for score in self.scoreboard:
                f.write(score)
                f.write("\n")