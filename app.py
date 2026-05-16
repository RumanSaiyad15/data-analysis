from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Read CSV file
    file_read = pd.read_csv('Online-Store-Orders.csv')
    
    # 1. Total revenue
    total_revenue = float(file_read['TotalPrice'].sum())
    
    # 2. Average order value
    average_order_value = float(file_read['TotalPrice'].mean())
    
    # 3. 3 Most popular products
    popular_products = file_read['Product'].value_counts().head(3)
    products_dict = {str(k): int(v) for k, v in popular_products.items()}
    
    # 4. Top 5 customers
    top_customers = file_read['CustomerID'].value_counts().head(5)
    customers_dict = {str(k): int(v) for k, v in top_customers.items()}
    
    # 5. Orders by city
    orders_by_city = file_read['ShippingAddress'].value_counts().head(10)
    city_dict = {str(k): int(v) for k, v in orders_by_city.items()}
    
    # 6. Payment method distribution
    payment_methods = file_read['PaymentMethod'].value_counts()
    payment_dict = {str(k): int(v) for k, v in payment_methods.items()}
    
    # 7. Order status distribution
    order_status = file_read['OrderStatus'].value_counts()
    status_dict = {str(k): int(v) for k, v in order_status.items()}
    
    # 8. Pending order quantity
    pending_order_quantity = int(file_read[file_read['OrderStatus'] == 'pending']['Quantity'].sum())
    
    # 9. Unique customers
    unique_customers = int(file_read['CustomerID'].nunique())
    
    # 10. Most expensive product
    most_expensive_idx = file_read['UnitPrice'].idxmax()
    most_expensive_product = file_read.loc[most_expensive_idx]
    expensive_product_name = str(most_expensive_product['Product'])
    expensive_product_price = float(most_expensive_product['UnitPrice'])
    
    # Total orders
    total_orders = len(file_read)
    
    data = {
        'total_revenue': total_revenue,
        'average_order_value': round(average_order_value, 2),
        'total_orders': total_orders,
        'unique_customers': unique_customers,
        'pending_quantity': pending_order_quantity,
        'expensive_product': expensive_product_name,
        'expensive_product_price': expensive_product_price,
        'popular_products': products_dict,
        'top_customers': customers_dict,
        'orders_by_city': city_dict,
        'payment_methods': payment_dict,
        'order_status': status_dict,
    }
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
