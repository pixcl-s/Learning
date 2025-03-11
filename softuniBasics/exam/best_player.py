
# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч
# от световното първенство. Информацията, която получавате ще бъде играч
# и колко гола е отбелязал. От вас се иска да отпечатате кой е играчът с
# най-много голове и дали е направил хет-трик.
# Хет-трик е, когато футболистът е вкарал 3 или повече гола.
# Ако футболист е вкарал 10 или повече гола, програмата трябва да спре.


# От конзолата се четат по два реда до въвеждане на команда "END":
# Име на играч – текст
# Брой вкарани голове  – цяло положително число в интервала [1 … 10000]

# На конзолата да се отпечатат 2 реда :
# На първия ред:
#      	"{име на играч} is the best player!"
# На втория ред :
#  Ако най-добрият футболист е направил хет-трик:
#          	"He has scored {брой голове} goals and made a hat-trick !!!"
# Ако най-добрият футболист НЕ е направил хет-трик:
#                    	"He has scored {брой голове} goals."

football_player = input()


best_player = ""
best_player_goals = 0

while football_player != "END":

    goals_scored = int(input())

    if goals_scored > best_player_goals:
        best_player = football_player
        best_player_goals = goals_scored

    if goals_scored >= 10:
        break

    football_player = input()

print(f"{best_player} is the best player!")

if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
