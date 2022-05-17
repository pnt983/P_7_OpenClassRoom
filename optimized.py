from utils import get_actions_objects_from_csv, during_time


def get_sorted_percent(csv):
    """Get csv and sort by percent"""
    actions_list = get_actions_objects_from_csv(csv)
    # actions_list.sort(key=lambda action: action.percent, reverse=True)
    return actions_list


@during_time
def get_best_invest(csv_file):
    csv_list_sorted = get_actions_objects_from_csv(csv_file, sort_list=True)
    action_name = ""
    total_cost = 0
    total_profit = 0
    for action in csv_list_sorted:
        if total_cost + action.cost > 500:
            continue
        elif total_cost < 500:
            action_name += action.name
            total_cost += action.cost
            total_profit += action.profit
        else:
            break
    print("Resultat: ", action_name, total_cost, total_profit)


def main():
    get_best_invest("data_files/dataset2.csv")


if __name__ == "__main__":
    main()
