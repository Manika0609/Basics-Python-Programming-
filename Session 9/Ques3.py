def amount(func):
    def inner(P, R, T):
        interest = func(P, R, T)
        amount = P + interest
        return amount
    return inner
def SI(P, R, T):
    interest = (P * R * T)/100
    return interest
ref = amount(SI)
P = int(input("Enter Amount:"))
R = int(input("Enter Rate:"))
T = int(input("Enter Time:"))
print(ref(P, R, T))
