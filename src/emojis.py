ZERO = "0⃣️"
ONE = "1⃣️"
TWO = "2⃣"
THREE = "3⃣️"
FOUR = "4⃣"
FIVE = "5⃣"
SIX = "6⃣"
SEVEN = "7⃣"
EIGHT = "8⃣"
NINE = "9⃣"
TEN = "🔟"

def number_to_emoji(score):
    if score == 0:
        return ZERO
    elif score == 1:
        return ONE
    elif score == 2:
        return TWO
    elif score == 3:
        return THREE
    elif score == 4:
        return FOUR
    elif score == 5:
        return FIVE
    elif score == 6:
        return SIX
    elif score == 7:
        return SEVEN
    elif score == 8:
        return EIGHT
    elif score == 9:
        return NINE
    elif score == 10:
        return TEN

troll_emojis = ["🅱️", "🍆", "🍑", "😹", "😏", "💩", "🤪"]