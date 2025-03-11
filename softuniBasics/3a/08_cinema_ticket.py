
# Да се напише програма която чете ден от седмицата (текст) –
# въведен от потребителя и принтира на конзолата цената на
# билет за кино според деня от седмицата:
# Monday	Tuesday	   Wednesday	Thursday	Friday	Saturday	Sunday
#   12	       12	       14	       14	      12	   16      	  16

day = input().lower()

if day == "monday" or day == "tuesday" or day == "friday":
    print(12)
elif day == "wednesday" or day == "thursday":
    print(14)
elif day == "saturday" or day == "sunday":
    print(16)
else:
    print(error)
