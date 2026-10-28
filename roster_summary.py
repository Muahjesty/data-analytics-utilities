from collections import defaultdict

def main():
    # dict to hold list of gpa, creds tuples for diff majors
    major_data = defaultdict(list)
    
    # read input file
    with open("roster1.dat", "r") as f:
        for line in f:
            if line.strip():
                name, major, gpa, credits = line.strip().split(",")
                major_data[major].append((float(gpa), int(credits)))
                
    # write input
    with open("roster1.out", "w") as f:
        for major, records in major_data.items():
            count = len(records)
            avg_gpa = sum(r[0] for r in records) / count
            avg_credits = sum(r[1] for r in records) / count
            
            # write- major, avgGpa, avgCredits, count
            f.write(f"{major},{avg_gpa:.2f},{avg_credits:.2f},{count}\n")

if __name__ == "__main__":
    main()