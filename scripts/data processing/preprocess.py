import pandas as pd
import os

# Đường dẫn tới file CSV gốc
data_path = os.path.join("data","raw", "vietnam_population_2011_2016.csv")
output_path = os.path.join("data", "cleaned", "cleaned_population.csv")

# Đọc dữ liệu từ file CSV
try:
    data = pd.read_csv(data_path)
    print("Đọc dữ liệu thành công.")
except Exception as e:
    print(f"Lỗi khi đọc file: {e}")
    exit()

# Kiểm tra cột
print("Danh sách cột:", data.columns)

# Làm sạch dữ liệu
try:
    # Loại bỏ khoảng trắng trong tên cột nếu có
    data.rename(columns=lambda x: x.strip(), inplace=True)

    # Kiểm tra và chuyển đổi cột 'year' nếu cần
    if 'year' in data.columns:
        data['year'] = pd.to_numeric(data['year'], errors='coerce')  # Chuyển về dạng số

    # Kiểm tra giá trị bị thiếu
    print("Các giá trị bị thiếu:", data.isnull().sum())

    # Điền giá trị bị thiếu
    data = data.ffill().bfill()

    # Ghi file đã làm sạch
    data.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được làm sạch và lưu vào '{output_path}'.")
except Exception as e:
    print(f"Lỗi trong quá trình làm sạch dữ liệu: {e}")
