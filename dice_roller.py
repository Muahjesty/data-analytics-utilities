import sys
import random

def run_experiment():
    rolls = 0
    while True:
        rolls += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            return rolls

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hw2_p4.py <number_of_experiments>")
        return
        
    n = int(sys.argv[1])
    total_rolls = 0
    
    for _ in range(n):
        total_rolls += run_experiment()
        
    average_rolls = total_rolls / n
    print(f"{average_rolls:.2f}")

if __name__ == "__main__":
    main()