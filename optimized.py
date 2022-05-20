from utils import get_actions_objects_from_csv, during_time
from memory_profiler import profile
import cProfile


@profile
# @during_time
def get_best_invest(csv_file):
    rapport_list = []
    actions_list_sorted = get_actions_objects_from_csv(csv_file, sort_list=True)
    action_name = ""
    total_cost = 0
    total_profit = 0
    for action in actions_list_sorted:
        if total_cost + action.cost > 500:
            continue
        elif total_cost < 500:
            action_name += action.name
            total_cost += action.cost
            total_profit += action.profit
            rapport_list.append([action.name, action.cost, action.percent, action.profit])
        else:
            break
    print("Resultat: ", action_name, total_cost, total_profit)
    print(rapport_list)


def main():
    # get_best_invest("data_files/dataset1.csv")
    cProfile.run('get_best_invest("data_files/dataset1.csv")') 


if __name__ == "__main__":
    main()
