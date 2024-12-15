# scripts/analyze_trends.py
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_trends(input_path, output_path):
    """
    Phân tích xu hướng dân số qua các năm.
    
    Args:
        input_path (str): Đường dẫn dữ liệu đã lọc.
        output_path (str): Đường dẫn lưu biểu đồ xu hướng.
    """
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công cho phân tích xu hướng.")

        # Tổng dân số theo năm
        trend_data = data.groupby('Year')['Population grow ratio'].sum().reset_index()

        # Vẽ biểu đồ xu hướng
        plt.figure(figsize=(10,6))
        plt.plot(trend_data['Year'], trend_data['Population grow ratio'], marker='o', linestyle='-')
        plt.title("Xu hướng Dân số Việt Nam (2011-2020)")
        plt.xlabel("Năm")
        plt.ylabel("Tổng Dân số")
        plt.grid(True)
        plt.tight_layout()

        # Lưu biểu đồ
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
        plt.close()
        print(f"Biểu đồ xu hướng đã được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích xu hướng: {e}")

if __name__ == "__main__":
    input_csv = "data/cleaned/cleaned_population.csv"
    output_chart = "outputs/visualizations/Trend Analysis/example.png"
    analyze_trends(input_csv, output_chart)
