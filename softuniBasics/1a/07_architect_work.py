# Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта.
# Изготвянето на един проект отнема три часа.

architect = input()
projects = int(input())
hours = projects * 3

print(f"The architect {architect} will need {hours} hours to complete {projects} project/s.")
