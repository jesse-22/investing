# This program calculates the monthly amount of desired percentage
# of annual salary saved including interested collected on saved portion.
# The program also calculate how much of a down payment is needed depending
# on the total cost of the time.
# After, it will determine how many months is needed to reach the down payment
# of the house.

# Class to get the users annual salary
class Annual:
    def __init__(self, salary):
        self.salary = salary

    # Get salary from user
    def get_salary(self):
        return float(self.salary)

    # Output annual salary for verification
    def print_sal(self):
        print("Annual Salary", self.salary)


# Class to get users savings
class Savings:
    def __init__(self, savings):
        self.savings = savings

    def get_savings(self):
        return float(self.savings)

    # Output the user's desired savings percentage for verification
    def print_savings_percentage(self):
        print("Savings Percentage:", self.savings)

    # Output user's monthly monetary savings amount
    # This also includes the monthly interest made on saved portion
    def print_monthly_savings(self):
        s = self.get_monthly_savings()
        monthlyinterest = (s * 0.04) / 12
        monthlytotal = monthlyinterest + s
        print("Monthly portion saved:", monthlytotal)
        return float(monthlytotal)

    # Get user's monthly monetary amount before interest
    @staticmethod
    def get_monthly_savings():
        a = annual_a.get_salary()
        s = savings_a.get_savings()
        monthly = a * s
        return float(monthly)

    # Calculate the months it would take to reach total down payment amount
    @staticmethod
    def calculate_months():
        down = dp.calculate_downpayment()
        saved = savings_a.get_monthly_savings()
        totalmonths = down / saved
        print("Months to reach down payment:", totalmonths)


# Class to get the total cost of house
class TotalCost:
    def __init__(self, totalcost):
        self.totalcost = totalcost

    # Output the total cost of home for verification
    def print_total_cost(self):
        print("Total cost of home: ", self.totalcost)

    # Get the total cost of the home
    def get_total_cost(self):
        return float(self.totalcost)


# Class to get down payment for house
class DownPayment:
    def __init__(self, totalcost):
        self.totalcost = totalcost

    # Calculate the down payment needed from the
    # total cost of the home
    @staticmethod
    def calculate_downpayment():
        cost = tc.get_total_cost()
        downpayment = .25 * cost
        return float(downpayment)

    # Output down payment needed for verification
    def print_downpayment(self):
        down = self.calculate_downpayment()
        print("Down payment required:", down)


# Driver code
annual_a = Annual(input("Enter your annual salary:"))
annual_a.print_sal()
savings_a = Savings(input("Enter percent of annual salary you want to save in decimal format:"))
savings_a.print_savings_percentage()
savings_a.get_monthly_savings()
savings_a.print_monthly_savings()
tc = TotalCost(input("Enter total cost of home:"))
tc.print_total_cost()
tc.get_total_cost()
dp = DownPayment(tc)
dp.print_downpayment()
savings_a.calculate_months()
