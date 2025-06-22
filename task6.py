items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected = []
    total_cost = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected.append(name)
            total_cost += info["cost"]

    return selected


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]  
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    res = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name = item_list[i - 1][0]
            res.append(name)
            j -= item_list[i - 1][1]["cost"]

    return list(reversed(res))


if __name__ == "__main__":
    budget = 100

    print("Бюджет:", budget)
    print("Жадібний алгоритм:", greedy_algorithm(items, budget))
    print("Динамічне програмування:", dynamic_programming(items, budget))
