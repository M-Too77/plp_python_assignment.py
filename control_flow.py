def rate_performance(score):
    if score > 80:
        return "Distinction"
    elif 60 <= score <= 70:
        return "Credit"
    elif 40 <= score <= 50:
        return "Fair"
    else:
        return "Failed"

def main():
    try:
        score = float(input("Enter the student's score: "))
        if 0 <= score <= 100:
            performance = rate_performance(score)
            print(f"Performance: {performance}")
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

if __name__ == "__main__":
    main()

