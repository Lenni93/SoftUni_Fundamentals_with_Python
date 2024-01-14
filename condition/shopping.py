budget = int(input())
command = input()
while command != 'End':
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print("You bought everything needed.")
# 50
# 25
# 20
# 10
# 25 = 25 - 20 = 5 - 10 = -5 = you went overdraft
# 100
# 5
# End
# 100 - 5 = 95 and then is END  you bought everything needed