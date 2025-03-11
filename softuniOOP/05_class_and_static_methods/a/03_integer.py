# Create a class called Integer. Upon initialization, it should receive a single parameter value (int). It should have 3 additional methods:
#   · from_float(float_value) - creates a new instance by flooring the provided floating number.
#   If the value is not a float, return the message "value is not a float"
#   · from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
#   · from_string(value) - creates a new instance by converting the string to an integer
#   (if the value cannot be converted, return a message "wrong type")
from math import floor
from typing import Union


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> Union["Integer", str]:
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str) -> Union["Integer", str]:
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }
        the_int = 0
        for x in range(len(value)):
            if value[x] in roman_numerals:
                if x + 1 <= len(value)-1:
                    if roman_numerals[value[x]] < roman_numerals[value[x+1]]:
                        the_int -= roman_numerals[value[x]]
                    else:
                        the_int += roman_numerals[value[x]]
                else:
                    the_int += roman_numerals[value[x]]
            else:
                return "wrong type"
        else:
            return cls(the_int)

    @classmethod
    def from_string(cls, value: str) -> Union["Integer", str]:
        if isinstance(value, str):
            try:
                value = int(value)
                return cls(value)
            except ValueError:
                return "wrong type"
        else:
            return "wrong type"


# 100/100
# test
first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("XIX")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
# output
# 10
# 4
# value is not a float
# wrong type
