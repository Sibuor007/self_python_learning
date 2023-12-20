invest_rt = input("Enter investment amount:")
rate = input("Enter Investment rate: ")

invest_rt = float(invest_rt)
# rounds the interest rate to 2 decimal places.
rate = float(rate) * .01

for i in range(10):
    invest_rt = invest_rt + (invest_rt * rate)
print("Money invested after 10 years: {:.2f}".format(invest_rt))


