import json
from my_app.models import Customer, Work, Account

with open('data.json') as f:
    customers_inf = json.load(f)

for dict_inf in customers_inf:
    cust = Customer(name=dict_inf["name"], phone=dict_inf["phone"], email=dict_inf["email"])
    cust.save()
    cust.account_set.create(pin=dict_inf["pin"],
                            acc_num=dict_inf["acc_num"],
                            pan=dict_inf["pan"],
                            cvv=dict_inf["cvv"])
    cust.work_set.create(address=dict_inf["address"],
                         city=dict_inf["city"],
                         company=dict_inf["company"],
                         postalZip=dict_inf["postalZip"])


