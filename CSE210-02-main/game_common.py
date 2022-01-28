import random

class Game_Common():

    def __init__(self):
        self.current_turn = 0
        self.game_name = "Cards Galore!"
        self.player_score = 300

    def get_encouragement(self):
        return random.choice(["Good guess!", "Nice job!", "*clicks tongue* Noice.", "A masterpiece, really.", "This isn't your first rodeo, is it?", "You're a robot, you really are.",\
            "I wish I could guess numbers like you do.", "What a guess!", "Superb!", "Super sweet!", "Fantasticall!y done!", "Sweet!", "Nice throw!", "Stuff of royalty!"])

    def get_wrong_choice(self):
        return random.choice(["Not as lucky...", "Keep trying!", "What a loss!", "Getting there... but not quite there.", "Not the best guess.", "WOW...", "Not a winner, that one.",\
            "Target missed", "Negative on your last.", "Almost!", "No good!", "Unfortunate, really.", "Dissapointing... For you and the audience.", "You can do better than that!"])
    
    def get_tie_advice(self):
        return random.choice(["Looks like this round is a tie", "No points this round", "That't the same as the last card", "At least you're consistent", "Alright, we'll call it a draw", "So close", "I regret to inform you that no one has won"])

