import argparse
import matplotlib.pyplot as plt
import numpy as np
from sympy import isprime

def plot_function_with_primes(start_value):
    # Define the function
    def f(x):
        return start_value + x + x**2

    # Determine the maximum x so that f(x) <= 1,000,000
    x_max = int(np.floor((-1 + np.sqrt(1 + 4 * (1_000_000 - start_value))) / 2))

    # Generate x values
    x_vals = np.arange(0, x_max + 1)
    y_vals = f(x_vals)

    # Identify primes in the output
    prime_mask = np.array([isprime(y) for y in y_vals])
    prime_x = x_vals[prime_mask]
    prime_y = y_vals[prime_mask]

    # Plot all values
    plt.figure(figsize=(12, 6))
    plt.plot(x_vals, y_vals, color='lightgray', label=f'f(x) = {start_value} + x + x²')
    plt.scatter(prime_x, prime_y, color='crimson', s=5, label='Prime values')

    # Labels and legend
    plt.xlabel('x')
    plt.ylabel('f(x)')
    #plt.title(f'Plot of f(x) = {start_value} + x + x² with Prime Values Highlighted')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"poly_{start_value}.pdf", bbox_inches="tight")
#    plt.savefig(f"poly_{start_value}.svg", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot f(x) = a + x + x² and highlight primes.")
    parser.add_argument("start_value", type=int, help="The starting value (a) in the function.")
    args = parser.parse_args()

    plot_function_with_primes(args.start_value)

