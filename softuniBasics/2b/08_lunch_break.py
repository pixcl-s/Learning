
# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка,
# а времето за отдих ще бъде 1/4 от времето за почивка

import math

tv_show = input()
ep_length = int(input())
break_length = int(input())

lunch = break_length // 1/8
chill = break_length // 1/4

time_left = break_length - lunch - chill
leftover = time_left - ep_length


if time_left >= ep_length:
    print(f"You have enough time to watch {tv_show} and left with {math.ceil(leftover)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {math.ceil(abs(leftover))} more minutes.")
