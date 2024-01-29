invest_amount = input("Enter investment amount:")
rate = input("Enter Investment rate: ")

# typecasting input from user to float
invest_amount = float(invest_amount)
# rounds the interest rate to 2 decimal places.
rate = float(rate) * .01

# 10 iterations for 10 months of investment
for i in range(10):
    # add the interet to the intial investment amount one by one
    invest_amount += (invest_amount * rate)
# print the final investment after 10 years using the string.format
print("Money invested after 10 years: {:.2f}".format(invest_amount))
