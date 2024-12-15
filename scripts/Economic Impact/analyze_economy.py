import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import textwrap


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

        # 1. Xu hướng lực lượng lao động theo năm
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x='Year', y='15+ labor', marker='o', ci=None, color='blue')
        plt.title("Labor force trend (15+) by year", fontsize=17, color='blue')
        plt.xlabel("Year", fontsize=17)
        plt.ylabel("Labor force (15+)", fontsize=17)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "labor_trend.png"))
        plt.close()

        # 2. Mối liên hệ giữa lực lượng lao động và tăng trưởng dân số
        plt.figure(figsize=(15, 7))
        sns.scatterplot(data=data, x='15+ labor', y='Population grow ratio', hue='Region', palette='muted', s=100)  
        sns.regplot(data=data, x='15+ labor', y='Population grow ratio', scatter=False, color='red')
        plt.title("The relationship between labor force and population growth", fontsize=17, color='blue')
        plt.xlabel("15+ labor", fontsize=17)
        plt.ylabel("Population grow ratio (%)", fontsize=17)
        plt.legend(title="Region", title_fontsize=14, fontsize=12, loc='upper right')  
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "labor_vs_growth.png"))
        plt.close()

        # 3. Dân số trung bình theo khu vực
        plt.figure(figsize=(15, 6))
        sns.barplot(data=data, x='Region', y='Average population', ci=None, palette='coolwarm')
        plt.title("Average population by region", fontsize=17, color='blue')
        plt.xlabel("Region", fontsize=17)
        plt.ylabel("Average population", fontsize=17)
        regions = data['Region'].unique()
        plt.xticks(
            ticks=range(len(regions)),  
            labels=[textwrap.fill(label, 15) for label in regions],  
            rotation=0, 
            fontsize=12
        )
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "average_population_by_region.png"))
        plt.close()

        # 4. Mật độ dân số và tỷ lệ giới tính theo khu vực
        fig, ax1 = plt.subplots(figsize=(12, 6))
        sns.barplot(data=data, x='Region', y='Population density', ci=None, ax=ax1, color='skyblue')
        ax1.set_ylabel("Population density", fontsize=14)
        ax1.set_title("Population density and sex ratio by region", fontsize=17, color='blue')
        ax1.set_xlabel("Region", fontsize=16)
        regions = data['Region'].unique()
        ax1.set_xticklabels(
            [textwrap.fill(label, 15) for label in regions], 
            rotation=0, 
            fontsize=12
        )
        ax2 = ax1.twinx()
        sns.lineplot(data=data, x='Region', y='Sex ratio', ax=ax2, color='orange', marker='o', ci=None)
        ax2.set_ylabel("Sex ratio (%)", color='orange', fontsize=14)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "density_and_sex_ratio_by_region.png"))
        plt.close()

        # 5. Phân tích lực lượng lao động theo khu vực và theo năm
        # Chọn các cột phù hợp
        required_columns = ['Year', '15+ labor', 'Region']
        data = data[required_columns]

        # Chuyển đổi định dạng dữ liệu
        data['Year'] = data['Year'].astype(int)

        # Vẽ biểu đồ cột nhóm
        plt.figure(figsize=(15, 8))
        sns.barplot(data=data, x='Region', y='15+ labor', hue='Year', palette='viridis')

        # Tùy chỉnh biểu đồ
        plt.title("Labor Force (15+) by Region and Year", fontsize=16)
        plt.xlabel("Region", fontsize=14)
        plt.ylabel("15+ Labor Force", fontsize=14)
        plt.legend(title="Year", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "labor_force_by_region_and_year.png"))
        plt.close()

        print("Phân tích và lưu các biểu đồ hoàn tất!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")


if __name__ == "__main__":
    input_csv = "data/cleaned/cleaned_population.csv"  # Đường dẫn file CSV
    output_directory = "outputs/visualizations/Economic_Impact/Population_and_Economics"
    analyze_population_and_economics(input_csv, output_directory)
