# main.py
import os
from scripts.dataprocessing.preprocess import clean_data
from scripts.filter_data import filter_data
from scripts.analyze_trends import analyze_trends
from scripts.analyze_demographics import analyze_demographics
from scripts.analyze_economy import analyze_economy
from scripts.compare_years import compare_years

def main():
    # Đường dẫn file
    raw_csv = "data/raw/vietnam_population_2011_2016.csv"
    cleaned_csv = "data/cleaned/cleaned_population.csv"
    filtered_csv = "data/filtered/filtered_population.csv"
    visualizations_dir = "outputs/visualizations/"

    # Bước 1: Làm sạch dữ liệu
    print("Bước 1: Làm sạch dữ liệu...")
    clean_data(raw_csv, cleaned_csv)

    # Bước 2: Lọc dữ liệu (nếu cần, ví dụ: năm cụ thể hoặc tỉnh cụ thể)
    print("Bước 2: Lọc dữ liệu cho năm 2016...")
    filters = {'year': 2016}
    filter_data(cleaned_csv, filtered_csv, filters)

    # Bước 3: Phân tích xu hướng
    print("Bước 3: Phân tích xu hướng...")
    analyze_trends(cleaned_csv, os.path.join(visualizations_dir, "trend_population.png"))

    # Bước 4: Phân tích nhân khẩu học
    print("Bước 4: Phân tích nhân khẩu học...")
    analyze_demographics(cleaned_csv, visualizations_dir)

    # Bước 5: Phân tích tác động kinh tế
    print("Bước 5: Phân tích tác động kinh tế...")
    analyze_economy(cleaned_csv, visualizations_dir)

    # Bước 6: Phân tích so sánh
    print("Bước 6: Phân tích so sánh...")
    compare_years(cleaned_csv, visualizations_dir)

    # Bước 7: Tổng hợp báo cáo (Có thể thực hiện trong Jupyter Notebook)
    print("Bước 7: Tổng hợp báo cáo...")
    # Đây là bước thủ công, sử dụng notebooks hoặc công cụ báo cáo khác

    print("Dự án phân tích dữ liệu dân số hoàn thành.")

if __name__ == "__main__":
    main()
