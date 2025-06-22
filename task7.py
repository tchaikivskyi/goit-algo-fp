import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_rolls=1_000_000):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1
    
    probabilities = {k: (v / num_rolls) * 100 for k, v in sums_count.items()}
    
    return sums_count, probabilities

def print_probability_table(probabilities):
    print("| Сума | Імовірність (Монте-Карло) | Аналітична ймовірність |")
    print("|------|---------------------------|------------------------|")
    
    analytic_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    for sum_val in range(2, 13):
        print(f"| {sum_val:<4} | {probabilities[sum_val]:<25.2f}% | {analytic_probs[sum_val]:<22.2f}% |")

def plot_probabilities(probabilities):
    analytic_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    sums = list(range(2, 13))
    mc_probs = [probabilities[s] for s in sums]
    an_probs = [analytic_probs[s] for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar([s - 0.2 for s in sums], mc_probs, width=0.4, label='Монте-Карло')
    plt.bar([s + 0.2 for s in sums], an_probs, width=0.4, label='Аналітичні')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

sums_count, probabilities = monte_carlo_dice_simulation()

print("Результати симуляції методом Монте-Карло (1,000,000 кидків):")
print_probability_table(probabilities)
plot_probabilities(probabilities)