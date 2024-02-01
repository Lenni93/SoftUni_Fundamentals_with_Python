def solve(grade):
    if grade >= 2.00 and grade <= 2.99:
        return "Fail"
    elif grade >= 3.00 and grade <= 3.49:
        return "Poor"
    elif grade >= 3.50 and grade <= 4.49:
        return "Good"
    elif grade >= 4.50 and grade <= 5.49:
        return "Very Good"
    elif grade >= 5.50 and grade <= 6.00:
        return "Excellent"


graded = int(input())
result = graded
print(solve(grade))

# · 2.00 – 2.99 - "Fail"
# · 3.00 – 3.49 - "Poor"
# · 3.50 – 4.49 - "Good"
# · 4.50 – 5.49 - "Very Good"
# · 5.50 – 6.00 - "Excellent"
