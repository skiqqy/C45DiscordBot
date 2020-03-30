ZERO = "0️⃣️"
ONE = "1️⃣️"
TWO = "2️⃣️"
THREE = "3️⃣️"
FOUR = "4️⃣️"
FIVE = "5️⃣️"
SIX = "6️⃣️"
SEVEN = "7️⃣️"
EIGHT = "8️⃣️"
NINE = "9️⃣️"
TEN = "🔟️"

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

troll_emojis = ["🅱️", "🍆", "🍑️", "😹️", "😏️", "💩️", "🤪️"]