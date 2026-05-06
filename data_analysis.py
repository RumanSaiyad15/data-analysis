"""
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#                                           NUMMPY + PANDAS + MATPLOTLIB DATA ANALYSIS 
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
"""


# Pandas aur NumPy Questions (Data Analysis)
# -----------------------------------------------------------------------------------------------------------



# 1. Total revenue : Total revenue kitna hua
# -------------------------------------------------------------------------

import pandas as pd
import numpy as np

file_read = pd.read_csv('Online-Store-Orders.csv')
total_revenue = file_read['TotalPrice'].sum()
print(f'Total revenue is {total_revenue}')



# 2. Average order value : Average order value kitna hai
# ------------------------------------------------------------------------- 

average_order_value = file_read['TotalPrice'].mean()
print(f"Average order value is {average_order_value}")



# 3. 3 Most popular products : sabse jyada bikne wale 3 products kaun sa hai
# -------------------------------------------------------------------------

popular_products = file_read['Product'].value_counts().head(3)
print(f"3 most popular products are {popular_products}")



# 4. Top 5 customers : sabse jyada order karne wale 5 customers kaun hai
# -------------------------------------------------------------------------

popular_customers = file_read['CustomerID'].value_counts().head(5)
print(f"Top 5 customers are {popular_customers}")



# 5. Har city se kitne order aaye : har city se kitne order aaye hai
# -------------------------------------------------------------------------

orders_by_city = file_read['ShippingAddress'].value_counts()
print(f"Orders by city are {orders_by_city}")



# 6. Payment method distribution : kis payment method se kitne order aaye hai
# -------------------------------------------------------------------------

payment_method_distribution = file_read['PaymentMethod'].value_counts()
print(f"payment method distribution is {payment_method_distribution}")



# 7. Order status distribution : kitne order complete hai, kitne pending hai, kitne cancel hai
# -------------------------------------------------------------------------

order_status = file_read["OrderStatus"].value_counts()
print(f"order status distribution is {order_status}")



# 8. Shipping issue : pending order ki  quantity kitni hai 
# -------------------------------------------------------------------------

pending_order_quantity = file_read[file_read['OrderStatus'] == "pending"]["Quantity"].sum()
print(f"pending order quantity is {pending_order_quantity}")



# 9. Uniqe customer : unique customer kitne hai
# -------------------------------------------------------------------------

Unique_customer = file_read['CustomerID'].nunique()
print(f"unique customer is {Unique_customer}")



# 10. Sabse mahenga product : Sab se mahenga product konsa or kine ka hai 
# --------------------------------------------------------------------------

# .loc ka use tab karte hai jb hame row ya column ko unke name (label) se select karna ho 
most_expensive_product = file_read.loc[file_read["UnitPrice"].idxmin()]
print(f"most expensive product is  : {most_expensive_product['Product']} \n and its price is : {most_expensive_product['UnitPrice']}")



# 11. null value : kya koi null value hai data set me
# --------------------------------------------------------------------------

null_values = file_read.isnull().sum()
print(f"null values in each column are : \n {null_values}") 



# 12. referral source : har source se kitne 'Unique' (alag-alag) customers aaye hai
# --------------------------------------------------------------------------

referall_source = file_read.groupby('ReferralSource')['CustomerID'].nunique().sort_values(ascending=False)
print(f'which place new customer comes more {referall_source}')



# 13. stardard divison : quantity ka startdard divison kitna hai
# --------------------------------------------------------------------------

standard_division = np.std(file_read["Quantity"])
print(f"standard division of quantity is {standard_division}")




# (['OrderID', 'Date', 'CustomerID', 'Product', 'Quantity', 'UnitPrice',
#        'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'TrackingNumber',
#        'ItemsInCart', 'CouponCode', 'ReferralSource'  , 'TotalPrice']



# MATPLOTLIB VISUALIZATION
# -----------------------------------------------------------------------------------------------------------

# 14. revenue by product : har product se kitna revenue hua (bar chart)
# --------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

revenue_by_product = file_read.groupby("Product")["TotalPrice"].sum()
print(f"revenue by product is : \n {revenue_by_product}")

revenue_by_product.plot(kind='bar', figsize=(10, 6))
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 15. payment distubution : kis payment method se kitne order aaye hai (pie chart)
# --------------------------------------------------------------------------

payment_method_distribution = file_read["PaymentMethod"].value_counts()
print(f"payment method distribution is {payment_method_distribution}")

payment_method_distribution.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Payment Method Distribution')
plt.axis('equal')
plt.show()




# 16. order status distribution : kitne order complete hai, kitne pending hai, kitne cancel hai (bar chart)
# ----------------------------------------------------------------------------------------

order_status_distribution = file_read["OrderStatus"].value_counts()
print(f"order status distribution is {order_status_distribution}")
order_status_distribution.plot(kind='heatmap', cmap='viridis', figsize=(8, 6))
plt.title('Order Status Distribution')
plt.xlabel('Order Status')
plt.ylabel('Count')
plt.show()