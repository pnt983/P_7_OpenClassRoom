import csv
from time import perf_counter


class Action():

    def __init__(self, name, cost, percent):
        self.name = name
        self.cost = cost
        self.percent = percent

    @property
    def profit(self):
        return self.cost * self.percent / 100

    def __str__(self):
        return f"Name action: {self.name}, cost: {self.cost}, \
percent: {self.percent}%, profit: {self.profit}"


def get_actions_objects_from_csv(file_name, sort_list=False):
    """Return a list of Action object from a csv file"""
    actions = []
    with open(file_name, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            cost = float(row[1])
            percent = float(row[2])
            if cost <= 0.0 or percent <= 0:
                continue
            row[1] = cost
            row[2] = percent

            action = Action(row[0], cost, percent)
            actions.append(action)

    if sort_list:
        actions.sort(key=lambda action: action.percent, reverse=True)

    return actions


def during_time(func):
    """Time during the function is executed"""
    def wrapper(*args, **kawrgs):
        t1 = perf_counter()
        execute_function = func(*args, **kawrgs)
        t2 = perf_counter()
        print(f"Time during the function {func.__name__} was executed is: \
{round(t2 - t1, 4)} seconds")
        return execute_function
    return wrapper


def main():
    pass


if __name__ == "__main__":
    main()
