def safe_divide(a,b):
    try:
        div = a/b
    except ZeroDivisionError:
        print("Zero diviosn is not supported")
    except Exception as e:
        print(f"An error occurred: {e}")


safe_divide(5,0)