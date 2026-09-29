# Over-Current Protection System
# Simple Python simulation

class OverCurrentProtection:

    def __init__(self, current_limit):
        self.current_limit = current_limit

    def check_current(self, current):
        print("\n===== Over-Current Protection System =====")
        print(f"Load Current : {current:.2f} A")
        print(f"Safe Limit   : {self.current_limit:.2f} A")

        if current > self.current_limit:
            print("Status       : OVER-CURRENT")
            print("Protection   : ACTIVATED")
            print("Load         : DISCONNECTED")
            print("Alarm        : ON")
        else:
            print("Status       : NORMAL")
            print("Protection   : OFF")
            print("Load         : CONNECTED")
            print("Alarm        : OFF")


# Main Program
print("===== Over-Current Protection System =====")

limit = float(input("Enter maximum safe current (A): "))
current = float(input("Enter load current (A): "))

if limit <= 0 or current < 0:
    print("Invalid current value!")
else:
    protection = OverCurrentProtection(limit)
    protection.check_current(current)
