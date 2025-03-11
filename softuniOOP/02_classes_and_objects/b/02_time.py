# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers).
# The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59.
# You should also create 3 additional instance methods:
# - set_time(hours, minutes, seconds) - updates the time with the new values
# - get_time() - returns "{hh}:{mm}:{ss}"
# - next_second() - updates the time with one second (use the class attributes for validation) and
# returns the new time (use the get_time() method)

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        elif self.minutes < Time.max_minutes:
            self.seconds = 0
            self.minutes += 1
        elif self.hours < Time.max_hours:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        return self.get_time()


# 100/100
# test
time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

# output
# 09:31:00

# 11:00:00

# 00:00:00
