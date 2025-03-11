
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line.
# A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
# If a product passes the line and there is not a free robot to take it,
# it should be queued at the end of the line again.
# The robots are standing in line in the order of their appearance.
# Input
# On the first line, you will receive the robots' names and their processing times in the format
# "robotName-processTime;robotName-processTime;robotName-processTime..."
# On the second line, you will get the starting time in the format "hh:mm:ss"
# Next, until the "End" command, you will get a product on each line.
# Output
# Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

from collections import deque


def time(sec, m, h):
    sec += 1
    if sec == 60:
        m += 1
        sec = 0
        if m == 60:
            h += 1
            m = 0
            if h == 23:
                h = 0
    return sec, m, h


def busy_check(sec, busy):
    if sec in busy:
        del busy[sec]


def busy_check_for_robots(robo, busy):
    if robo in busy.values():
        return True
    else:
        return False


def current_robo(robos):
    while True:
        y, _ = robos[0].split("-")
        if busy_check_for_robots(y, busy_robot):
            robots.rotate(-1)
            continue
        else:
            free_robo, working = robos[0].split("-")
            break

    return free_robo, working


robots = deque(input().split(";"))
hours, minutes, seconds = [int(x) for x in input().split(":")]

products_queue = deque()
busy_robot = {}

while True:
    products = input()
    if products == "End":
        jump_to = min(busy_robot) - 1
        seconds = jump_to
        robots.rotate(-jump_to)
        products_queue.rotate(-jump_to)
        del busy_robot[min(busy_robot)]
        while products_queue:
            seconds, minutes, hours = time(seconds, minutes, hours)
            busy_check(seconds, busy_robot)
            if len(busy_robot) != len(robots):
                free_robot, work_time = current_robo(robots)
            if not busy_check_for_robots(free_robot, busy_robot):
                print(f"{free_robot} - {products_queue.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
                busy_until = seconds + int(work_time)
                if busy_until > 60:
                    busy_until -= 60
                busy_robot[busy_until] = free_robot
                robots.rotate(-1)
                continue
            products_queue.rotate(-1)
        break

    seconds, minutes, hours = time(seconds, minutes, hours)
    busy_check(seconds, busy_robot)

    if len(busy_robot) != len(robots):
        free_robot, work_time = current_robo(robots)

    if not busy_check_for_robots(free_robot, busy_robot):
        print(f"{free_robot} - {products} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
        busy_until = seconds + int(work_time)
        if busy_until > 60:
            busy_until -= 60
        busy_robot[busy_until] = free_robot
        robots.rotate(-1)
    else:
        products_queue.append(products)

# 66/100
