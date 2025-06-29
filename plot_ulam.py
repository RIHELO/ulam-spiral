import matplotlib.pyplot as plt
import sympy
import argparse


def generate_clockwise_spiral_coords(num,n):
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
   if num > n: return coords
  
   # RIGHT
   for _ in range(layer):
    x += 1
    coords[(x, y)] = num
    num += 1
    if num > n: return coords
   
   # DOWN
   for _ in range(layer):
    y -= 1
    coords[(x, y)] = num
    num += 1
    if num > n: return coords

   y = layer
   layer += 1
   x = 0

 return coords

def plot_clockwise_spiral_with_primes(starting_prime, n):
  coords = generate_clockwise_spiral_coords(starting_prime, n+starting_prime)
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

  diagonal_primes_count = 0
  total_diagonal_elements = 0

  for (x, y), val in coords.items():
    if x == y:  # Check if the coordinate is on the diagonal
        total_diagonal_elements += 1
        if val in prime_set:
            diagonal_primes_count += 1

  # Calculate the probability
  probability = diagonal_primes_count / total_diagonal_elements if total_diagonal_elements > 0 else 0

  plt.figure(figsize=(10, 10))
  plt.scatter(x_nonprimes, y_nonprimes, c='blue', label='Non-primes')
  plt.scatter(x_primes, y_primes, c='red', label='Primes')
  probability_text = f"Probability of primes on diagonal: {probability:.2f}"
  plt.text(0.5, 1.05, probability_text, ha='center', va='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

  plt.title(f"Initial prime {starting_prime} Clockwise Ulam Spiral Pattern up to {n} with Primes Highlighted")
  plt.axis('equal')
  plt.grid(True)
  plt.legend()
  plt.show()

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool")
    
    # Add parameters
    parser.add_argument("--initial", type=str, required=True, help="Initial prime number")
    parser.add_argument("--max", type=int, default=40000,  help="Max numbers to plot")

    args = parser.parse_args()

    plot_clockwise_spiral_with_primes(int(args.initial),int(args.max)) 

if __name__ == "__main__":
    main()
