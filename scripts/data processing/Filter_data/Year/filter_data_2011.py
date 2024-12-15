# scripts/filter_data.py
import pandas as pd
import os

def filter_data(input_path, output_path, filters):
    """
    Lọc dữ liệu theo các điều kiện được cung cấp.
    
    Args:
        input_path (str): Đường dẫn dữ liệu đã làm sạch.
        output_path (str): Đường dẫn lưu dữ liệu đã lọc.
        filters (dict): Các điều kiện lọc dưới dạng cột và giá trị.
                        Ví dụ: {'year': 2016, 'province': 'Hà Nội'}
    """
    try:
        # Đọc dữ liệu đã làm sạch
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu đã làm sạch thành công.")

        # Áp dụng các điều kiện lọc
        for column, value in filters.items():
            if isinstance(value, list):
                data = data[data[column].isin(value)]
            else:
                data = data[data[column] == value]

        # Lưu dữ liệu đã lọc
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Dữ liệu đã lọc và lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")

if __name__ == "__main__":
    input_csv = "data/cleaned/cleaned_population.csv"
    output_csv = "data/filtered/Year/filtered_population_2011.csv"
    filters = {
        'Year': 2016 # Lọc dữ liệu cho năm 2016
    }
    filter_data(input_csv, output_csv, filters)
