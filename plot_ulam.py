import matplotlib.pyplot as plt
import sympy
import argparse


def generate_clockwise_spiral_coords(num, n):
    coords = {}
    x, y = 0, 0
    coords[(x, y)] = num
    num += 1
    layer = 1

    while num <= n:
        # UP
        y += 1
        coords[(x, y)] = num
        num += 1
        if num > n:
            return coords

        # RIGHT
        for _ in range(layer):
            x += 1
            coords[(x, y)] = num
            num += 1
            if num > n:
                return coords

        # DOWN
        for _ in range(layer):
            y -= 1
            coords[(x, y)] = num
            num += 1
            if num > n:
                return coords

        y = layer
        layer += 1
        x = 0

    return coords


def plot_clockwise_spiral_with_primes(starting_prime, n, outname="spiral"):
    coords = generate_clockwise_spiral_coords(starting_prime, n + starting_prime)
    prime_set = set(sympy.primerange(starting_prime, n + starting_prime))

    x_primes, y_primes = [], []
    x_nonprimes, y_nonprimes = [], []

    for (x, y), val in coords.items():
        if val in prime_set:
            x_primes.append(x)
            y_primes.append(y)
        else:
            x_nonprimes.append(x)
            y_nonprimes.append(y)

    # Count diagonal primes
    diagonal_primes_count = 0
    total_diagonal_elements = 0
    for (x, y), val in coords.items():
        if x == y:
            total_diagonal_elements += 1
            if val in prime_set:
                diagonal_primes_count += 1

    probability = diagonal_primes_count / total_diagonal_elements if total_diagonal_elements > 0 else 0

    # Plot
    plt.figure(figsize=(10, 10))
    plt.scatter(x_nonprimes, y_nonprimes, c='lightgray', s=8, label="Non-primes")
    plt.scatter(x_primes, y_primes, c='red', s=8, label="Primes")

    plt.title(f"Ulam Spiral starting at {starting_prime}\nDiagonal prime density = {probability:.2f}")
    plt.axis("equal")
    plt.axis("off")
    plt.legend(loc="upper right")

    # Save as PDF + SVG for publication
    plt.savefig(f"{outname}_{starting_prime}.pdf", bbox_inches="tight")
    plt.savefig(f"{outname}_{starting_prime}.svg", bbox_inches="tight")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Generate Ulam spirals with prime highlights")
    parser.add_argument("--initial", type=int, required=True, help="Initial number")
    parser.add_argument("--max", type=int, default=100000, help="Max numbers to plot")
    args = parser.parse_args()

    plot_clockwise_spiral_with_primes(args.initial, args.max)


if __name__ == "__main__":
    main()
