"""
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#                                           PANDAS AND NUMPY DATA SET
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
"""

import pandas as pd
import numpy as np

file_read = pd.read_csv('Online-Store-Orders.csv')
print(file_read)
# total colunm
column = file_read.columns
print(column)
# 1 . find total revenue
total_revenue = file_read['TotalPrice'].sum()
print(f'total revenue is {total_revenue}')


#  Iska breakdown step-by-step dekho:
# -->  file_read.groupby('ProductName'): Sabse pehle, yeh data ko product ke naam ke hisaab se "groups" mein baant deta hai 
#      (saare 'iPhone' ek saath, saare 'Laptop' ek saath).
# -->  ['Revenue']: Ab hum sirf 'Revenue' waale column par focus kar rahe hain, kyunki humein kamayi check karni hai.
# -->  .sum(): Yeh har group ke saare revenue amounts ko jod (add) deta hai. Matlab, har product ki total sales value nikal jaati hai.
# .idxmax(): Yeh sabse important part hai. Yeh check karta hai ki kis product ka sum sabse bada (maximum) hai aur uska naam (ID) return karta hai.
# print(f'...'): Finally, f-string use karke re

# 2. find best selling product  
# ------------------------------------------------------------------------------
# -->  groupby('ProductName') kya karta hai: Woh computer ko bolta hai ki "Saare Mobiles ko ek dhabbe mein rakho, 
# saare Laptops ko doosre dhabbe mein, aur saare Watches ko teesre dhabbe mein.

# -->  idxmax kyun use hota hai?
# Seedhi baat: Sabse badi value ka Naam (Index) dhoondhne ke liye.

# Aksar log max() aur idxmax() mein confuse hote hain. Inka farak dekhiye:

# max(): Yeh aapko sirf number batayega. (Maano, sabse zyada 500 quantity biki, toh result aayega 500). Par kaunsa product bika? Yeh nahi batayega.
# idxmax(): Yeh aapko us line ka Label/Naam batayega jahan sabse badi value hai. (Result aayega: "Mobile").
# best_selling_product = file_read.groupby('ProductName')['Quantity'].sum().idxmax()
# print(f'best selling product is {best_selling_product}')

best_selling_product = file_read.groupby('Product')['Quantity'].sum().idxmax()
print(f'best selling product is {best_selling_product}') 


#  3  customer behaveior analysis
# ek customer avg kitne iteam kharidta hai
# ------------------------------------------------------------------------------

# Agar aap .mean() use karte hain:

# Toh right side mein Average Items dikhte hain (Matlab woh har baar jab aata hai, toh lagbhag kitne items saath le jata hai).

# Example: Maan lijiye ek customer ne 2 baar shopping ki: ek baar 2 items liye aur ek baar 8 items.

# .sum() dikhayega: 10 (Total items)
# .mean() dikhayega: 5 (Average per visit)

average_items_per_customer = file_read.groupby('CustomerID')['Quantity'].mean()
print(average_items_per_customer)


# 4 conversion : kis referal source se zyada customer aa rahe hai 
#                (instagram, google, direct ) 
# -------------------------------------------------------------------------
# Yeh apne aap count bhi karega aur zyada se kam (Descending order) mein sort bhi kar dega

# Agar aapko yeh dekhna hai ki "Paisa kidhar se zyada aa raha hai", 
# toh value_counts() dekhein.
best_referral_source = file_read['ReferralSource'].value_counts()

print(f"which place money comes more {best_referral_source}")





# Yeh ginega ki har source se kitne 'Unique' (alag-alag) customers aaye
referral_analysis = file_read.groupby('ReferralSource')['CustomerID'].nunique().sort_values(ascending=False)
print(f'which place new customer comes more {referral_analysis}')


# Agar aapko yeh dekhna hai ki "Naye log kidhar se zyada jud rahe hain", 
# toh nunique() 

# ascending=True: Chhote se Bada (1, 2, 3, 4, 5...)
# ascending=False: Bade se Chhota (5, 4, 3, 2, 1...)


# 5. Shipping issue : kitne order pending hai 
# -------------------------------------------------------------------------

pending_orders = file_read[file_read['OrderStatus']=='Pending']
print(pending_orders)


# 6. coupon impact : kya log coupon code use kar rahe hai ya nahi
# -------------------------------------------------------------------------

coupon_impact = file_read['CouponCode'].value_counts()
print(f'coupon impact is {coupon_impact}')

"""
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#                                           MATPLOTLIB DATA SET
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
"""



import matplotlib as plt
import pandas as pd
df = pd.read_csv ("Online-Store-Orders.csv")

total_product = len(df)  # TOTAL ROW
print(total_product)


unique_products = df['Product'].nunique()  
print("total unique product", unique_products) # how many total unique products
print("product name",df['Product'].unique())   # unique product name 
print(unique_products)

# PRODUCT NAME AND THERE SELLS QUANTITY
# -------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

file_read = pd.read_csv("Online-Store-Orders.csv")

# har product ki total sales 
grouped = df.groupby("Product")['Quantity'].sum()

# Top 7 products (optional)
top_products =  grouped.sort_values(ascending=False).head(7)

# Graph 
top_products.plot(kind='bar') # kind means which graph you want to display

plt.title("Top selling Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.legend()
plt.show()


