import numpy as np
import pandas as pd

def calculate_inventory(df, predictions):
    df['Predicted'] = predictions
    
    lead_time = 5
    service_level = 1.65
    
    std_dev = df['Sales'].std()
    safety_stock = service_level * std_dev * np.sqrt(lead_time)
    
    df['Reorder_Point'] = df['Predicted'] * lead_time + safety_stock
    
    return df