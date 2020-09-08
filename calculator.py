f_n = float(input())
act = input()
s_n = float(input())
if act == "+":
    dec = f_n + s_n
elif act == "-":
    dec = f_n - s_n
elif act == "*":
    dec = f_n * s_n
elif act == "/":
    dec = f_n / s_n
print(dec)