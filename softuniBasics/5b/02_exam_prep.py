
# Напишете програма, в която Марин решава задачи от изпити,
# докато не получи съобщение "Enough" от лектора си. При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда "Enough" или
# ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка,
# която е по-малка или равна на 4.

# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6]

# ⦁	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# ⦁	"Average score: {средна оценка}"
# ⦁	"Number of problems: {броя на всички задачи}"
# ⦁	"Last problem: {името на последната задача}"
# ⦁	Ако получи определеният брой незадоволителни оценки:
# ⦁	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

poor_grades_limit = int(input())
task = input()

sum_tasks = 0
grade_sum = 0
poor_grades = 0

while task != "Enough":
    last_task = task
    grade = int(input())
    sum_tasks += 1
    grade_sum += grade
    if grade <= 4:
        poor_grades += 1
        if poor_grades == poor_grades_limit:
            print(f"You need a break, {poor_grades} poor grades.")
            exit()
    task = input()

print(f"Average score: {(grade_sum / sum_tasks):.2f}")
print(f"Number of problems: {sum_tasks}")
print(f"Last problem: {last_task}")
