coins=[2000,500,100,50,20,10,5,2,1]
def change_given(amount):
    for i in coins:
        times = amount // i
        amount = amount % i
        print(f"note:{i}; count {times}")
        if amount == 0:
            break 

#change_given(5000)



aval_bal={2000:10, 500:30, 100:20, 50:40, 20:20, 10:100, 5:50, 2:1000, 1:2000}
def change_given_ad(amount):
    for i in aval_bal:
        times = amount // i
        amount = amount % i
        aval_bal.update({i:aval_bal[i]-times})
        if amount == 0:
            break

    print(aval_bal)
change_given_ad(5758585000)