import csv
import random
import os
from datetime import datetime, timedelta
from collections import defaultdict

# Створюємо папку для даних, якщо її не існує
output_dir = 'synthetic_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Папку '{output_dir}' створено.")

# Set seed for reproducibility
random.seed(42)

# Constants
USER_IDS = list(range(1001, 1201))  # 200 users
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Event types and their funnel progression
EVENT_TYPES = ['page_view', 'product_viewed', 'add_to_cart', 'initiate_checkout', 'purchase', 'cart_abandoned', 'account_created']
PRODUCT_CATEGORIES = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports', 'Beauty']
PAYMENT_METHODS = ['credit_card', 'paypal', 'apple_pay', 'google_pay']
ORDER_STATUSES = ['completed', 'refunded', 'cancelled']
CHANNELS = ['paid_search', 'paid_social', 'organic', 'email', 'referral', 'social_media']
COUNTRIES = ['USA', 'UK', 'Canada', 'Ukraine'] # Додав Україну для цікавості

# Product names by category
PRODUCTS = {
    'Electronics': ['iPhone 15', 'Samsung Galaxy S24', 'MacBook Pro', 'Dell XPS', 'Sony Headphones', 'iPad Air', 'Apple Watch', 'Kindle'],
    'Clothing': ['Blue Jeans', 'Winter Jacket', 'Running Shoes', 'Cotton T-Shirt', 'Dress Shirt', 'Sneakers', 'Hoodie', 'Sweater'],
    'Home': ['Coffee Maker', 'Blender', 'Vacuum Cleaner', 'Air Purifier', 'Table Lamp', 'Cookware Set', 'Bed Sheets', 'Towel Set'],
    'Books': ['The Great Novel', 'Python Programming', 'Data Science Guide', 'Business Strategy', 'Self Help Book', 'Mystery Novel', 'Biography', 'Cookbook'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Running Belt', 'Tennis Racket', 'Basketball', 'Resistance Bands', 'Gym Bag', 'Water Bottle'],
    'Beauty': ['Face Cream', 'Shampoo', 'Lipstick', 'Foundation', 'Perfume', 'Body Lotion', 'Hair Serum', 'Nail Polish']
}

# Helper functions
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def get_price(category):
    price_ranges = {
        'Electronics': (299, 2499), 'Clothing': (19, 199), 'Home': (29, 399),
        'Books': (9, 49), 'Sports': (15, 299), 'Beauty': (12, 149)
    }
    return round(random.uniform(*price_ranges[category]), 2)

# --- ГЕНЕРАЦІЯ USER EVENTS ---
print("Generating user_events.csv...")
user_events = []
event_id, session_id = 1, 1000
user_purchase_dates = defaultdict(list)

for user_id in USER_IDS:
    activity_level = random.choice(['low', 'medium', 'high'])
    num_sessions = {'low': random.randint(1, 3), 'medium': random.randint(4, 8), 'high': random.randint(9, 20)}[activity_level]
    user_start_date = random_date(START_DATE, END_DATE - timedelta(days=30))

    user_events.append({
        'event_id': event_id, 'user_id': user_id, 'event_timestamp': user_start_date.strftime('%Y-%m-%d %H:%M:%S'),
        'event_type': 'account_created', 'session_id': session_id, 'page_url': '/signup', 'product_id': ''
    })
    event_id += 1; session_id += 1

    for _ in range(num_sessions):
        session_date = random_date(user_start_date + timedelta(days=1), END_DATE)
        session_id += 1
        num_events = random.randint(3, 15)

        for page_num in range(random.randint(2, 5)):
            user_events.append({
                'event_id': event_id, 'user_id': user_id, 'event_timestamp': (session_date + timedelta(minutes=page_num * 2)).strftime('%Y-%m-%d %H:%M:%S'),
                'event_type': 'page_view', 'session_id': session_id, 'page_url': random.choice(['/home', '/products', '/deals']), 'product_id': ''
            })
            event_id += 1

        viewed_products = [random.randint(5001, 5200) for _ in range(random.randint(1, 4))]
        for view_num, p_id in enumerate(viewed_products):
            user_events.append({
                'event_id': event_id, 'user_id': user_id, 'event_timestamp': (session_date + timedelta(minutes=10 + view_num * 3)).strftime('%Y-%m-%d %H:%M:%S'),
                'event_type': 'product_viewed', 'session_id': session_id, 'page_url': f'/product/{p_id}', 'product_id': p_id
            })
            event_id += 1

        funnel_progress = random.random()
        if funnel_progress > 0.3 and viewed_products:
            cart_items = random.sample(viewed_products, k=random.randint(1, min(3, len(viewed_products))))
            for cart_item in cart_items:
                user_events.append({
                    'event_id': event_id, 'user_id': user_id, 'event_timestamp': (session_date + timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S'),
                    'event_type': 'add_to_cart', 'session_id': session_id, 'page_url': f'/product/{cart_item}', 'product_id': cart_item
                })
                event_id += 1

            if funnel_progress > 0.6:
                user_events.append({
                    'event_id': event_id, 'user_id': user_id, 'event_timestamp': (session_date + timedelta(minutes=25)).strftime('%Y-%m-%d %H:%M:%S'),
                    'event_type': 'initiate_checkout', 'session_id': session_id, 'page_url': '/checkout', 'product_id': ''
                })
                event_id += 1

                if funnel_progress > 0.75:
                    purchase_time = session_date + timedelta(minutes=30)
                    user_events.append({
                        'event_id': event_id, 'user_id': user_id, 'event_timestamp': purchase_time.strftime('%Y-%m-%d %H:%M:%S'),
                        'event_type': 'purchase', 'session_id': session_id, 'page_url': '/checkout/complete', 'product_id': ''
                    })
                    user_purchase_dates[user_id].append(purchase_time)
                    event_id += 1
                else:
                    user_events.append({
                        'event_id': event_id, 'user_id': user_id, 'event_timestamp': (session_date + timedelta(minutes=27)).strftime('%Y-%m-%d %H:%M:%S'),
                        'event_type': 'cart_abandoned', 'session_id': session_id, 'page_url': '/checkout', 'product_id': ''
                    })
                    event_id += 1

with open(os.path.join(output_dir, 'user_events.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['event_id', 'user_id', 'event_timestamp', 'event_type', 'session_id', 'page_url', 'product_id'])
    writer.writeheader()
    writer.writerows(user_events)

# --- ГЕНЕРАЦІЯ TRANSACTIONS ---
print("Generating transactions.csv...")
transactions = []
order_id = 10001
purchasing_users = list(user_purchase_dates.keys())

for user_id in purchasing_users:
    for purchase_date in user_purchase_dates[user_id]:
        for _ in range(random.randint(1, 4)):
            category = random.choice(PRODUCT_CATEGORIES)
            unit_price = get_price(category)
            qty = random.randint(1, 3)
            total = round(qty * unit_price, 2)
            transactions.append({
                'order_id': order_id, 'user_id': user_id, 'order_date': purchase_date.strftime('%Y-%m-%d'),
                'product_category': category, 'product_name': random.choice(PRODUCTS[category]),
                'quantity': qty, 'unit_price': unit_price, 'total_amount': total,
                'discount_amount': round(total * random.uniform(0.05, 0.20), 2) if random.random() > 0.7 else 0,
                'payment_method': random.choice(PAYMENT_METHODS),
                'order_status': random.choices(['completed', 'refunded', 'cancelled'], weights=[90, 7, 3])[0]
            })
            order_id += 1

with open(os.path.join(output_dir, 'transactions.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['order_id', 'user_id', 'order_date', 'product_category', 'product_name', 'quantity', 'unit_price', 'total_amount', 'discount_amount', 'payment_method', 'order_status'])
    writer.writeheader()
    writer.writerows(transactions)

# --- ГЕНЕРАЦІЯ MARKETING SPEND ---
print("Generating marketing_spend.csv...")
marketing_data = []
current_date = START_DATE
while current_date <= END_DATE:
    for channel in CHANNELS:
        for country in COUNTRIES:
            base_spend = {'paid_search': 1500, 'paid_social': 1200, 'organic': 50, 'email': 150, 'referral': 100, 'social_media': 700}[channel]
            spend = round(base_spend * random.uniform(0.5, 1.5) * (1.5 if current_date.month in [11, 12] else 1.0), 2)
            impressions = int(spend * random.uniform(500, 1500))
            marketing_data.append({
                'date': current_date.strftime('%Y-%m-%d'), 'acquisition_channel': channel,
                'spend_amount': spend, 'impressions': impressions, 'clicks': int(impressions * random.uniform(0.01, 0.05)),
                'country': country
            })
    current_date += timedelta(days=1)

with open(os.path.join(output_dir, 'marketing_spend.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['date', 'acquisition_channel', 'spend_amount', 'impressions', 'clicks', 'country'])
    writer.writeheader()
    writer.writerows(marketing_data)

print(f"\nГотово! Файли збережено в папку: {os.path.abspath(output_dir)}")