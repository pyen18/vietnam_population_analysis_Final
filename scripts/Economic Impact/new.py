import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_population_and_economics(input_path, output_dir):
    """
    Phân tích dữ liệu dân số và các yếu tố kinh tế liên quan.

    Args:
        input_path (str): Đường dẫn file CSV.
        output_dir (str): Thư mục lưu các biểu đồ kết quả.
    """
    try:
        # Đọc dữ liệu
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        # Kiểm tra các cột cần thiết
        required_columns = ['Year', '15+ labor', 'Population grow ratio', 
                            'Region', 'Average population', 'Population density', 'Sex ratio']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        # Tạo thư mục lưu trữ kết quả nếu chưa tồn tại
        os.makedirs(output_dir, exist_ok=True)

        # Group data by Region and calculate summary statistics for relevant columns
        region_summary = data.groupby('Region').agg({
            'Population density': ['mean', 'min', 'max'],
            'Average population': ['mean', 'min', 'max'],
            '15+ labor': ['mean', 'min', 'max'],
            'Population grow ratio': ['mean', 'min', 'max']
        }).reset_index()

        region_summary.columns = [
            'Region', 
            'Density_mean', 'Density_min', 'Density_max',
            'Population_mean', 'Population_min', 'Population_max',
            'Labor_mean', 'Labor_min', 'Labor_max',
            'Growth_mean', 'Growth_min', 'Growth_max'
        ]

        # Set up the plotting style
        plt.style.use('seaborn-darkgrid')

        # Plotting Population Density by Region
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # 1. Population Density
        axes[0, 0].bar(region_summary['Region'], region_summary['Density_mean'], color='skyblue')
        axes[0, 0].set_title('Average Population Density by Region', fontsize=14)
        axes[0, 0].set_ylabel('Density (people/km²)', fontsize=12)
        axes[0, 0].tick_params(axis='x', rotation=45)

        # 2. 15+ Labor Force
        axes[0, 1].bar(region_summary['Region'], region_summary['Labor_mean'], color='orange')
        axes[0, 1].set_title('Average Labor Force (15+) by Region', fontsize=14)
        axes[0, 1].set_ylabel('Labor Force (thousands)', fontsize=12)
        axes[0, 1].tick_params(axis='x', rotation=45)

        # 3. Population Growth Ratio
        axes[1, 0].bar(region_summary['Region'], region_summary['Growth_mean'], color='green')
        axes[1, 0].set_title('Average Population Growth Ratio by Region', fontsize=14)
        axes[1, 0].set_ylabel('Growth Ratio (%)', fontsize=12)
        axes[1, 0].tick_params(axis='x', rotation=45)

        # 4. Average Population 
        axes[1, 1].bar(region_summary['Region'], region_summary['Population_mean'], color='purple')
        axes[1, 1].set_title('Average Population by Region', fontsize=14)
        axes[1, 1].set_ylabel('Population (thousands)', fontsize=12)
        axes[1, 1].tick_params(axis='x', rotation=45)

        # Adjust layout and save the plot
        plt.tight_layout()
        output_file = os.path.join(output_dir, 'population_analysis.png')
        plt.savefig(output_file)
        plt.show()

        print("Phân tích và lưu các biểu đồ hoàn tất!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")

if __name__ == "_main_":
    input_csv = "data/cleaned/cleaned_population.csv"  # Đường dẫn file CSV
    output_directory = "outputs/visualizations/Economic_Impact/Newest"
    analyze_population_and_economics(input_csv, output_directory)