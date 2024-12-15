import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def predict_population_linear(input_path):
    # Đọc dữ liệu
    data = pd.read_csv(input_path)
    print("Dữ liệu đã được đọc thành công.")
    
    # Lấy các cột cần thiết
    X = data['Year'].values.reshape(-1, 1)
    y = data['Average population'].values.reshape(-1, 1)
    
    # Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Mô hình hồi quy tuyến tính
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Dự đoán
    y_pred = model.predict(X_test)
    print(f"MSE: {mean_squared_error(y_test, y_pred)}")
    
    # Dự đoán dân số cho 10 năm tiếp theo
    future_years = np.arange(data['Year'].max() + 1, data['Year'].max() + 11).reshape(-1, 1)
    future_population = model.predict(future_years)
    
    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Dữ liệu gốc', color='blue')
    plt.plot(X_test, y_pred, label='Dự đoán', color='red')
    plt.plot(future_years, future_population, label='Dự đoán tương lai', linestyle='--', color='green')
    plt.xlabel('Year')
    plt.ylabel('Average Population')
    plt.title('Population Prediction Using Linear Regression')
    plt.legend()
    plt.show()

    return future_years, future_population

# Gọi hàm
input_csv = "data/cleaned/cleaned_population.csv"
predict_population_linear(input_csv)
