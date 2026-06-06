is_cold = False
is_warm = False
if is_warm:
    print("It's a warm day")
    print("Drink plenty of water")
elif is_cold:
       print("wear warm clothes")
       print("wear jackets")
else:
       print("have a lovely day")
price = 1000000
buyer_has_credit = False
if buyer_has_credit:
    down_payment = 0.1 * price
    print(f"down payment: ${down_payment}")
else:
    down_payment = 0.2 * price
has_income = True
has_credit = True
has_criminal_record = False
if has_income and has_credit and not has_criminal_record:
    print("Eligible for loan")
temperature = 28
if temperature > 30:
    print("it's a hot day")
else:
    print("its a cold day")
name = "Liam Smith"
if len(name) < 3:
    print("name must be atleast 3 characters")
elif len(name) > 50:
    print("name must be less than 50 characters")
else:
    print("Name looks good!")