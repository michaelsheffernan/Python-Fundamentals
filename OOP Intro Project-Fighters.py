import random


class Fighter:

    def __init__(self, name, age, weight, belt):
        self.name = name
        self.age = age
        self.weight = weight
        self.belt = belt

    def display_info(self):
        print(f'''
              Fighter Record {self.name}:
              Age: {self.age}
              Weight: {self.weight}
              Belt: {self.belt}
              ''')

    def train(self, hours):
        print(f"{self.name} trained for {hours} hours.")
        training_hours = 0
        training_hours += hours
        return training_hours


class BJJStudent(Fighter):

    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses

    def compete(self):
        w_or_l = random.randrange(1, 4)
        if w_or_l == 1:
            print(f"{self.name} won. Adding to record (:")
            self.wins += 1

        elif w_or_l == 2:
            print(f"{self.name} lost. Adding to record ):")
            self.losses += 1

        elif w_or_l == 3:
            print(f"{self.name} drew. No change to record |:")

    def show_record(self):
        print(f"{self.name}'s record is {self.wins} wins and {self.losses} losses.")


fighter1 = Fighter("Michael", 17, 75, "White Belt")
fighter1.display_info()
fighter1.train(10)
fighter1 = BJJStudent("Michael", 0, 0)
fighter1.compete()
fighter1.show_record()
