import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", periods=200)
products = ["Milk", "Bread", "Eggs"]
stores = ["Store_A", "Store_B"]

data = []

for store in stores:
    for product in products:
        base = np.random.randint(50, 100)
        trend = np.linspace(0, 20, 200)
        seasonality = 10 * np.sin(np.arange(200) / 10)
        
        price = np.random.randint(20, 50)
        
        sales = base + trend + seasonality + np.random.randint(-10, 10, 200)
        
        for i in range(200):
            data.append([
                dates[i], store, product,
                int(sales[i]), price
            ])

df = pd.DataFrame(data, columns=["Date","Store","Product","Sales","Price"])
df.to_csv("data/raw/sales.csv", index=False)

print("Advanced dataset created!")
exit()