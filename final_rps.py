import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']


class Player:
    def __init__(self):

        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass


class RandomPlayer(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)


class Cycles(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = moves[0]
        if self.step % 5 == 0:
            throw = moves[0]
            self.step += 1
        elif self.step % 5 == 1:
            throw = moves[1]
            self.step += 1
        elif self.step % 5 == 2:
            throw = moves[2]
            self.step += 1
        elif self.step % 5 == 3:
            throw = moves[3]
            self.step += 1
        elif self.step % 5 == 4:
            throw = moves[4]
            self.step += 1
        return throw


class ReflectPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            throw = moves[0]
        else:
            throw = self.learn_move
            return (throw)

    def learn(self, learn_move):

        self.learn_move = learn_move


class HumanPlayer(Player):

    def move(self):

        throw = input('rock, paper, scissors, lizard, spock? \n').lower()

        while (throw != 'rock'and throw != 'paper'and throw != 'scissors'
                and throw != 'lizard' and throw != 'spock'):
            print('Sorry try again! \n')
            throw = input('rock, paper, scissors, lizard, spock? \n').lower()
        return (throw)


class Game:
    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):
        round = 1
        print("Let's Begin!")
        while True:
            print(f"Round {round}:")
            self.play_round()
            while True:
                c = input("Do you want to continue? (y/n): \n")
                if c.lower() != 'y' and c.lower() != 'n':
                    continue
                else:
                    break
            if c.lower() == 'y':
                continue
            elif c.lower() == 'n':
                break
        if self.p1.score > self.p2.score:
            print('Player 1 won!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a draw!')
        print(f"The final score is P1: {self.p1.score} P2: {self.p2.score}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play(self, move1, move2):
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if beats(move1, move2) == "w":
            print("** PLAYER ONE WINS! **")
            print(f"Score: Player 1: {self.p1.score}  Player 2: "
                  f"{self.p2.score}\n")
            self.p1.score += 1
            return 1
        elif beats(move1, move2) == "l":
            print("** PLAYER TWO WINS! **")
            print(f"Score: Player 1: {self.p1.score}  Player 2: "
                  f"{self.p2.score}\n")
            self.p2.score += 1
            return 2
        elif beats(move1, move2) == "d":
            print("** It's A DRAW! **")
            print(f"Score: Player 1: {self.p1.score}  Player 2: "
                  f"{self.p2.score}\n")
            return 0


def beats(one, two):
    if one == 'rock':
        if two == 'rock':
            return "d"
        elif two == 'spock':
            return "l"
        elif two == 'lizard':
            return "w"
        elif two == 'paper':
            return "l"
        elif two == 'scissors':
            return "w"
    elif one == 'paper':
        if two == 'paper':
            return "d"
        elif two == 'spock':
            return "w"
        elif two == 'lizard':
            return "l"
        elif two == 'rock':
            return "w"
        elif two == 'scissors':
            return "l"
    elif one == 'scissors':
        if two == 'scissors':
            return "d"
        elif two == 'spock':
            return "l"
        elif two == 'lizard':
            return "w"
        elif two == 'rock':
            return "l"
        elif two == 'paper':
            return "w"
    elif one == 'lizard':
        if two == 'lizard':
            return "d"
        elif two == 'spock':
            return "w"
        elif two == 'scissors':
            return "l"
        elif two == 'rock':
            return "l"
        elif two == 'paper':
            return "w"
    elif one == 'spock':
        if two == 'spock':
            return "d"
        elif two == 'lizard':
            return "l"
        elif two == 'scissors':
            return "w"
        elif two == 'rock':
            return "w"
        elif two == 'paper':
            return "l"


if __name__ == '__main__':
    p2 = input('Select the RPSLS you\'d like to play: \n'
               '[1]Rock [2]Random [3]Cycles or [4]Reflect \n')
    while True:
        if p2 == '1':
            p2 = Player()
            break
        elif p2 == '2':
            p2 = RandomPlayer()
            break
        elif p2 == '3':
            p2 = Cycles()
            break
        elif p2 == '4':
            p2 = ReflectPlayer()
            break
        else:
            p2 = input('Select the RPSLS you\'d like to play: \n'
                       '[1]Rock, [2]Random, [3]Reflective, or [4]Cycles \n')

    Game = Game(p2)
    Game.play_game()
