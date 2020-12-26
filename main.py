from food import Food
from food import add_food
from process_data import read_data
from process_data import add_data

def message(text: str):
    screen_width=100
    box_width = 30
    box_space = (box_width - len(text)*2) // 2
    left_margin = (screen_width - box_width ) //2
    print("\n" + " " * left_margin + "+" + "-" * (box_width) + "+")
    print(" " * left_margin +"|" + " " * (box_width) + "|")
    print(" " * left_margin +"|" + " " * (box_space) + text + " " * (box_space) + "|")
    print(" " * left_margin +"|" + " " * (box_width) + "|")
    print(" " * left_margin +"+" + "-" * (box_width) + "+\n")

message("你的冰箱里现在有")
read_data()

message("要记录今天的菜篮吗？")
print("\n(1) 是")
print("(2) 否")
usr_choice = input("-> ")
if usr_choice == "1":
    food = Food()
    my_fridge = add_food(food)
    add_data(my_fridge)
    read_data()
else:
    exit()