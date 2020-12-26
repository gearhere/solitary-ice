class Food:
    def __init__(self):
        self.name = input("请输入食品名称：")
        self.bought_place = input("请输入购买地点：")
        self.best_before = input("请输入食品最佳食用日期：")

def add_food(new_food) -> dict:
    my_fridge = read_data()
    store_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    my_fridge[new_food.name] = {
        "bought place": new_food.bought_place,
        "store time": store_time,
        "best before": new_food.best_before
        }
    return my_fridge