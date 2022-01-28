from time import sleep
from card import Card
from game_common import Game_Common

class Card_Game():
    
    def __init__(self):
        self.common_data = Game_Common()
        self.name = input(str("What is your username/display name? "))
        print(f"\n\nWelcome to {self.common_data.game_name}, {self.name}!")
        self.new_card = Card()
        self.prev_card = Card()
        self.play_again = ""
        self.advice = ""
        self.guess_state = ""

    def start_game(self):
        print("You will begin the game with 300 point. \nEach round you will guess if the next card in the deck is higher or lower than the last\n"
        "\nYou earn 100 points if you guess right and loose 75 if you guess wrong.\n")
        sleep(0.5)
        print("I'll go ahead and draw the first card...")
        self.play_round()

    def play_round(self):
        self.common_data.current_turn += 1 #iterate the round count
        self.draw_new_cards()
        print(f"\nThe last card you drew was a {self.prev_card.card_value}") #tell the player which card was drawn last round
        guess = input(str("Will the next card be higher or lower [h/l]? ")).lower() #ask if they think the next card will be higher or lower
        if self.new_card.card_value > self.prev_card.card_value and guess == "h": #if they correctly guessed it would be higher
            self.guess_state = "correct"
            score = self.update_score() #update the players score
            self.advice = self.common_data.get_encouragement()
        elif self.new_card.card_value < self.prev_card.card_value and guess == "l":  #if they correctly guessed it would be lower
            self.guess_state = "correct"
            score = self.update_score() #update the players score
            self.advice = self.common_data.get_encouragement()
        elif self.new_card.card_value == self.prev_card.card_value: #if the next card drawn is the same as the last one
            self.guess_state = "same card"
            score = self.update_score()
            self.advice = self.common_data.get_tie_advice()
        else:
            self.guess_state = "wrong"
            score = self.update_score() #update the players score
            self.advice = self.common_data.get_wrong_choice()
        
        print(f"You drew a {self.new_card.card_value}; {self.advice}") #tell the player which card was drawn and give them some advice
        
        if score > 0: #if the player has more than 0 points
            if self.common_data.current_turn == 1:
                print(f'Your score is {score} after {self.common_data.current_turn} round.')
                self.ask_play_again()
            else:
                print(f"Your score is {score} after {self.common_data.current_turn} rounds.") #print the players score and the round counter
                self.ask_play_again()
        else: #if the player has less than 0 points, the game is over
            self.end_game()

    def ask_play_again(self):
        self.play_again = str(input("Would you like to play again (Y/N)? ")).lower()
        if self.play_again == "y" or self.play_again == "yes":
            self.play_round() #start another round
        else: 
            self.end_game()        

    def update_score(self):
        if self.guess_state == "correct":
            self.common_data.player_score += 100
            return self.common_data.player_score
        elif self.guess_state == "same card":
            return self.common_data.player_score
        else:
            self.common_data.player_score -= 75
            return self.common_data.player_score

    def end_game(self):
        self.play_again = str(input("Would you like to play another game (Y/N)? ")).lower()
        if self.play_again == "y" or self.play_again =="yes":
            game = Card_Game()
            game.start_game()
        else:
            print ("Thanks for playing! Bye.")

    def draw_new_cards(self):
        if self.common_data.current_turn == 1: #for first round, draw two cards
            self.prev_card.draw_new_card()
            self.new_card.draw_new_card()
        else: #for all rounds after the first, set the previous card equal to the card you drew last round, then draw one new card.
            self.prev_card = self.new_card
            self.new_card = Card()

if __name__ == "__main__":
    game = Card_Game()
    game.start_game()
