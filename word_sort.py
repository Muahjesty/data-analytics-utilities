import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hw2_p2.py <filename>")
        return
        
    filename = sys.argv[1]
    all_words = []
    
    with open(filename, "r") as f:
        for line in f:
            # split by whitespace to keep words like there's
            all_words.extend(line.strip().split())
            
    # sort case insensitively 
    all_words.sort(key=str.lower)
    
    # print one word for each line
    for word in all_words:
        print(word)

if __name__ == "__main__":
    main()