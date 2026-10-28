import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hw2_p3.py <filename>")
        return
        
    filename = sys.argv[1]
    word_count = 0
    
    with open(filename, "r") as f:
        for line in f:
            words = line.strip().split()
            word_count += len(words)
            
    print(word_count)

if __name__ == "__main__":
    main()