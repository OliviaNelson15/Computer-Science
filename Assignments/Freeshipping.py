#Amazon free shipping eligibility system
#Prime customers OR purchases for over $25
#(If under 18, you need parent consent to purchase.)
#This program will determine weather or not you are eligable for free shipping on your order.

#Ask for purchase amount, prime status, age, and parent consent.

def free_shipping(purchase_amount, prime_status, age, parent_consent):
    if (prime_status == True  or purchase_amount >=25) and (age >= 18 or parent_consent == True):
        print("You are eligable! Free shipping has been applied toyour order.")
    else:
        print("Ineligible for free shipping.")

parent_consent = False
purchase_amount = 50
age = 12
prime_status = False

free_shipping(parent_consent, purchase_amount, age, prime_status)