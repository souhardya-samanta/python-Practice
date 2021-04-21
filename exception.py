try:
    age=int(input("Enter Age "))
    income=int(input("Enter income "))
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Entered value must be integer")