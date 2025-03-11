
# Магазин за плодове през работните дни работи на следните цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	 2.50	 1.20	 0.85	   1.45 	2.70	  5.50   	 3.85

# През събота и неделя магазинът работи на по-високи цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	 2.70	1.25	0.90	  1.60	    3.00	  5.60	     4.20

# Напишете програма, която чете от конзолата следните три променливи,
# въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
# плод | ден от седмицата | количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

fruit = input()
day = input().lower()
quantity = float(input())

if day == "saturday" or day == "sunday":
    if fruit == "banana":
        print(f"{quantity * 2.70:.2f}")
    elif fruit == "apple":
        print(f"{quantity * 1.25:.2f}")
    elif fruit == "orange":
     print(f"{quantity * 0.90:.2f}")
    elif fruit == "grapefruit":
        print(f"{quantity * 1.60:.2f}")
    elif fruit == "kiwi":
     print(f"{quantity * 3.00:.2f}")
    elif fruit == "pineapple":
        print(f"{quantity * 5.60:.2f}")
    elif fruit == "grapes":
     print(f"{quantity * 4.20:.2f}")
    else:
        print("error")
elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if fruit == "banana":
        print(f"{quantity * 2.50:.2f}")
    elif fruit == "apple":
        print(f"{quantity * 1.20:.2f}")
    elif fruit == "orange":
     print(f"{quantity * 0.85:.2f}")
    elif fruit == "grapefruit":
        print(f"{quantity * 1.45:.2f}")
    elif fruit == "kiwi":
     print(f"{quantity * 2.70:.2f}")
    elif fruit == "pineapple":
        print(f"{quantity * 5.50:.2f}")
    elif fruit == "grapes":
     print(f"{quantity * 3.85:.2f}")
    else:
        print("error")
else:
    print("error")
