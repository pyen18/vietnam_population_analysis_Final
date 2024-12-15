# scripts/compare_years.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def compare_years(input_path, output_dir):
    """
    So sánh các chỉ số nhân khẩu học và kinh tế qua các năm.
    
    Args:
        input_path (str): Đường dẫn dữ liệu đã làm sạch.
        output_dir (str): Thư mục lưu các biểu đồ.
    """
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công cho phân tích so sánh.")

        # So sánh dân số qua các năm
        plt.figure(figsize=(10,6))
        sns.lineplot(x='Year', y='Population grow ratio', data=data, marker='o')
        plt.title("So sánh Dân số qua các năm")
        plt.xlabel("Năm")
        plt.ylabel("Tổng Dân số")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "compare_population_years.png"))
        plt.close()
        print("Biểu đồ so sánh dân số qua các năm đã được lưu.")

        # So sánh các chỉ số kinh tế nếu có
        economic_columns = ['gdp', 'unemployment_rate']
        for col in economic_columns:
            if col in data.columns:
                plt.figure(figsize=(10,6))
                sns.lineplot(x='year', y=col, data=data, marker='o')
                plt.title(f"So sánh {col.capitalize()} qua các năm")
                plt.xlabel("Năm")
                plt.ylabel(col.capitalize())
                plt.grid(True)
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f"compare_{col}_years.png"))
                plt.close()
                print(f"Biểu đồ so sánh {col} qua các năm đã được lưu.")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích so sánh: {e}")

if __name__ == "__main__":
    input_csv = "data/cleaned/cleaned_population.csv"
    output_directory = "outputs/visualizations/"
    compare_years(input_csv, output_directory)
