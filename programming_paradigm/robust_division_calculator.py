def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError:
        return "Please enter numeric values only."




