import time
import random


def print_sleep(pr, s):
    print(pr)
    time.sleep(s)


def intro():
    print_sleep("You are the owner of a new cellphone "
                "company, you have to take appropriate "
                "decisions to maximize profits and "
                "balance before the game ends! \n", 3)
    print_sleep("As you proceed in the game, you will be "
                "unlocking levels, think wisely where to "
                "spend the money!\n", 3)
    print_sleep("Your on your own now, Good Luck! \n", 2)


def design_smartphone(bal, level):
    print_sleep("Time to design your new smartphone! \n", 2)
    print_sleep(f"Your balance is: {bal}\n", 2)
    print_sleep("ENTER APPROPRIATE NUMBERS! \n", 2)
    li = ['0', '0', '0', '0', '0', '0']
    if level == 1:
        level1(li, bal, level)
    elif level == 2:
        level2(li, bal, level)
    elif level == 3:
        level3(li, bal, level)


def level1(li, balance, lvl):
    while li[0] not in ['1', '2']:
        print_sleep("Select body: \n", 2)
        li[0] = input("1. Polycarbonate: 5000\n"
                      "2. Alluminium : 10000\n")
    while li[1] not in ['1', '2']:
        print_sleep("Select display: \n", 2)
        li[1] = input("1. LCD 360x480 : 5000\n"
                      "2. LED 360x480 : 10000\n")
    while li[2] not in ['1', '2']:
        print_sleep("Select camera resolution: \n", 2)
        li[2] = input("1. R:5mp F:VGA: 5000\n"
                      "2. R:8mp F:3.2mp: 10000\n")
    while li[3] not in ['1', '2']:
        print_sleep("Select processor: \n", 2)
        li[3] = input("1. Mediatek 110k : 5000\n"
                      "2. Snapdragon 450 : 10000\n")
    while li[4] not in ['1', '2']:
        print_sleep("Select ram n rom: \n", 2)
        li[4] = input("1. 1+8gb : 5000\n"
                      "2. 2+16gb : 10000\n")
    while li[5] not in ['1', '2']:
        print_sleep("Select battery: \n", 2)
        li[5] = input("1. 2500mAh: 5000\n"
                      "2. 2850mAh : 10000\n")
    lvl += 1
    estimate(li, balance, lvl)


def level2(li, balance, lvl):
    while li[0] not in ['1', '2', '3']:
        print_sleep("Select body: \n", 2)
        li[0] = input("1. Polycarbonate : 5000\n"
                      "2. Alluminium : 10000\n"
                      "3. Glass : 15000\n")
    while li[1] not in ['1', '2', '3']:
        print_sleep("Select display: \n", 2)
        li[1] = input("1. LCD 360x720 : 5000\n"
                      "2. LED 480x720 : 10000\n"
                      "3. OpticAmoLED 720x1080: 15000\n")
    while li[2] not in ['1', '2', '3']:
        print_sleep("Select camera resolution: \n", 2)
        li[2] = input("1. R:5mp F:VGA: 5000\n"
                      "2. R:8mp F:3.2mp: 10000\n"
                      "3. R:13mp F:5mp: 15000\n")
    while li[3] not in ['1', '2', '3']:
        print_sleep("Select processor: \n", 2)
        li[3] = input("1. Mediatek 110k : 5000\n"
                      "2. Snapdragon 450 : 10000\n"
                      "3. Exynos 8812 : 15000\n")
    while li[4] not in ['1', '2', '3']:
        print_sleep("Select ram n rom: \n", 2)
        li[4] = input("1. 1+8gb : 5000\n"
                      "2. 2+16gb : 10000\n"
                      "3. 3+32gb : 15000\n")
    while li[5] not in ['1', '2', '3']:
        print_sleep("Select battery: \n", 2)
        li[5] = input("1. 2500mAh: 5000\n"
                      "2. 2850mAh : 10000\n"
                      "3.3500mAh : 15000\n")
    lvl += 1
    estimate(li, balance, lvl)


def level3(li, balance, lvl):
    while li[0] not in ['1', '2', '3', '4']:
        print_sleep("Select body: \n", 2)
        li[0] = input("1. Polycarbonate : 5000\n"
                      "2. Alluminium : 10000\n"
                      "3. Glass : 15000\n"
                      "4. Transperant Glass: 20000\n")
    while li[1] not in ['1', '2', '3', '4']:
        print_sleep("Select display: \n", 2)
        li[1] = input("1. LCD 360x720 : 5000\n"
                      "2. LED 480x720 : 10000\n"
                      "3. OpticAmoLED 720x1080 : 15000\n"
                      "4. SuperAmoLED 1080x1920: 20000\n")
    while li[2] not in ['1', '2', '3', '4']:
        print_sleep("Select camera resolution: \n", 2)
        li[2] = input("1. R:5mp F:VGA: 5000\n"
                      "2. R:8mp F:3.2mp: 10000\n"
                      "3. R:13mp F:5mp: 15000\n"
                      "4. R:20mp F:12mp: 20000\n")
    while li[3] not in ['1', '2', '3', '4']:
        print_sleep("Select processor: \n", 2)
        li[3] = input("1. Mediatek 110k : 5000\n"
                      "2. Snapdragon 450 : 10000\n"
                      "3. Exynos 8812 : 15000\n"
                      "4. AMDExynos 10000: 20000\n")
    while li[4] not in ['1', '2', '3', '4']:
        print_sleep("Select ram n rom: \n", 2)
        li[4] = input("1. 1+8gb : 5000\n"
                      "2. 2+16gb : 10000\n"
                      "3. 3+32gb : 15000\n"
                      "4. 4+64gb : 20000\n")
    while li[5] not in ['1', '2', '3', '4']:
        print_sleep("Select battery: \n", 2)
        li[5] = input("1. 2500mAh: 5000\n"
                      "2. 2850mAh : 10000\n"
                      "3. 3500mAh : 15000\n"
                      "4. 4000mAh : 20000\n")
    lvl += 1
    estimate(li, balance, lvl)


def estimate(choices, balance, lvl):
    cost = 0
    for i in choices:
        if i == '1':
            cost += 5000
        elif i == '2':
            cost += 10000
        elif i == '3':
            cost += 15000
        else:
            cost += 20000
    balance -= cost
    print_sleep(f"Your overall cost is: {cost}\n", 2)
    release(balance, cost, lvl)


def release(bal, c, level):
    comment = [
        "Brilliant Design",
        "Astonishing Performance",
        "Could have been better",
        "It's my fav device",
        "Amazing battery",
        "Classy camera",
        "okayish",
        "As expected",
        "I'd not use it even for free"]
    if level == 1 and c > 40000:
        prof = 10 * c
    elif level == 2 and c > 65000:
        prof = 30 * c
    elif level == 3 and c > 85000:
        prof = 100 * c
    else:
        prof = random.randint(0, 100) * c
    print_sleep(f"Verdict is out: {random.choice(comment)}\n", 2)
    print_sleep(f"Your profit is: {prof}\n", 2)
    bal += prof
    next_level(bal, level)


def next_level(balance, lvl):
    while lvl < 4:
        print_sleep(f"Congratulations! You are now level {lvl}!\n", 2)
        design_smartphone(balance, lvl)
    if balance > 5000000:
        print_sleep(f"Congratulations, You Win! You have "
                    f"sucessfully maximized profits and balance! "
                    f"Your highscore is: {balance}\n", 2)
        continuee()
    else:
        print_sleep("So sorry, You failed to maximize the profits!"
                    " Better luck next time!\n", 2)
        continuee()


def continuee():
    choice = input("Do you want to play again? (y/n)\n", 2)
    if choice.lower() == "y":
        start()
    elif choice.lower() == "n":
        exit(0)
    else:
        print_sleep("Please enter appropriate choice! \n", 2)
        continuee()


def start():
    intro()
    design_smartphone(60000, 1)


start()
