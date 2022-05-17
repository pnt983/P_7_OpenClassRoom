from itertools import combinations
from utils import get_actions_objects_from_csv, during_time
from memory_profiler import profile
import cProfile

@during_time
def get_all_combinations(data):
    """Return all combination possible from a list"""
    all_combi = []
    for n in range(1, len(data) + 1):
        combinaisons = combinations(data, n)
        for combi in combinaisons:
            all_combi.append(combi)
    return all_combi

# @profile
@during_time
def create_list_profit(all_combi):
    results_list = []
    for combinaison in all_combi:
        action_name = ""
        total_cost = 0
        total_profit = 0
        for i in combinaison:
            action_name += i.name
            total_cost += i.cost
            total_profit += i.profit
            if total_cost >= 500:
                break
        if total_cost < 500:
            result_invest = {"actions": action_name, "cost": total_cost,
                             "profit": total_profit}
            results_list.append(result_invest)
    results_list.sort(key=lambda i: i["profit"], reverse=True)
    return results_list


def main():
    file_csv = get_actions_objects_from_csv("data_files/20_actions.csv")
    all_combinaison = get_all_combinations(file_csv)
    all_profits = create_list_profit(all_combinaison)
    print(all_profits[0])


if __name__ == "__main__":
    main()
