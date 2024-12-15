
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_population_density(input_path, output_folder):
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        required_columns = ['Year', 'Population density', 'Region']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        # Group population density by year and region
        density_data = data.groupby(['Year', 'Region'])['Population density'].mean().unstack()
        os.makedirs(output_folder, exist_ok=True)

        # 1. Grouped bar chart for population density
        bar_width = 0.15
        years = density_data.index.astype(str)
        regions = density_data.columns
        x = np.arange(len(years))

        plt.figure(figsize=(12, 6))
        for i, region in enumerate(regions):
            plt.bar(x + i * bar_width, density_data[region], width=bar_width, label=region)

        plt.title("Vietnam's population density (2011-2020)", fontsize=14)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("population density (people/Square kilometer)", fontsize=12)
        plt.xticks(x + bar_width * (len(regions) / 2 - 0.5), years, fontsize=10)
        plt.legend(title="Region", fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.6, axis='y')
        plt.tight_layout()
        group_bar_chart_path = os.path.join(output_folder, "population_density_group_bar_chart.png")
        plt.savefig(group_bar_chart_path)
        plt.show()
        plt.close()

        # 2. Individual bar charts for each region
        for region in regions:
            plt.figure(figsize=(10, 6))
            plt.bar(density_data.index.astype(str), density_data[region], color='skyblue', alpha=0.8)
            plt.title(f"Vietnam's population density {region} (2011-2020)", fontsize=14)
            plt.xlabel("Years", fontsize=12)
            plt.ylabel("population density (people/km²)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6, axis='y')
            plt.tight_layout()
            region_chart_path = os.path.join(output_folder, f"population_density_{region}.png")
            plt.savefig(region_chart_path)
            plt.show()
            plt.close()

        print("Phân tích và lưu tất cả biểu đồ thành công!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")


def analyze_average_population(input_path, output_path):
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        required_columns = ['Year', 'Average population']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        average_population_data = data.groupby('Year')['Average population'].mean()
        years = average_population_data.index.astype(str)
        populations = average_population_data.values

        plt.figure(figsize=(10, 6))
        plt.bar(years, populations, color='skyblue', alpha=0.8)
        plt.title("Vietnam's average population (2011-2020)", fontsize=14)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("average populationh (thousand people)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6, axis='y')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.show()
        plt.close()

        print("Phân tích và lưu biểu đồ thành công!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")


def analyze_population_by_region(input_path, output_folder):
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        required_columns = ['Year', 'Region', 'Average population']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        region_population_data = data.groupby(['Year', 'Region'])['Average population'].mean().unstack()
        os.makedirs(output_folder, exist_ok=True)

        for region in region_population_data.columns:
            plt.figure(figsize=(10, 6))
            plt.bar(region_population_data.index.astype(str), region_population_data[region], color='orange', alpha=0.8)
            plt.title(f"Average population at {region} (2011-2020)", fontsize=14)
            plt.xlabel("Years", fontsize=12)
            plt.ylabel("average population (thousand people)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6, axis='y')
            plt.tight_layout()
            region_chart_path = os.path.join(output_folder, f"average_population_{region}.png")
            plt.savefig(region_chart_path)
            plt.show()
            plt.close()

        print("Phân tích và lưu biểu đồ dân số trung bình theo vùng thành công!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")

def analyze_natural_population_growth(input_path, output_folder):
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        required_columns = ['Year', 'Population density', 'Region']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        # Sort the data by year
        data_sorted = data.sort_values(by='Year')
        # Calculate the population growth rate as a percentage change
        data_sorted['Population Growth Rate'] = data_sorted.groupby('Region')['Population density'].pct_change() * 100

        # Calculate the growth rate by year (averaging across all regions)
        growth_rate_by_year = data_sorted.groupby('Year')['Population Growth Rate'].mean()
        
        # Make sure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # 1. Bar chart of population growth rate by year for the whole country
        years = growth_rate_by_year.index.astype(str)
        growth_rates = growth_rate_by_year.values

        plt.figure(figsize=(10, 6))
        plt.bar(years, growth_rates, color='lightcoral', alpha=0.8)
        plt.title("Vietnam's natural population growth rate (2011-2020)", fontsize=14)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("population growth rate (%)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6, axis='y')
        plt.tight_layout()
        year_growth_rate_chart = os.path.join(output_folder, "natural_population_growth_rate_by_year.png")
        plt.savefig(year_growth_rate_chart)
        plt.show()
        plt.close()

        # 2. Bar charts of population growth rate by region across years
        growth_rate_by_region = data_sorted.groupby(['Year', 'Region'])['Population Growth Rate'].mean().unstack()

        for region in growth_rate_by_region.columns:
            plt.figure(figsize=(10, 6))
            plt.bar(growth_rate_by_region.index.astype(str), growth_rate_by_region[region], color='lightgreen', alpha=0.8)
            plt.title(f"Natural population growth rate at {region} (2011-2020)", fontsize=14)
            plt.xlabel("Years", fontsize=12)
            plt.ylabel("population growth rate (%)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6, axis='y')
            plt.tight_layout()
            region_growth_rate_chart = os.path.join(output_folder, f"natural_population_growth_rate_{region}.png")
            plt.savefig(region_growth_rate_chart)
            plt.show()
            plt.close()

        print("Phân tích và lưu biểu đồ tỷ lệ tăng dân số tự nhiên thành công!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")

def analyze_labor_force(input_path, output_folder):
    try:
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công!")

        required_columns = ['Year', 'Region', '15+ labor']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        labor_force_data = data.groupby(['Year', 'Region'])['15+ labor'].mean().unstack()
        os.makedirs(output_folder, exist_ok=True)

        # 1. Grouped bar chart for labor force by region over time
        bar_width = 0.15
        years = labor_force_data.index.astype(str)
        regions = labor_force_data.columns
        x = np.arange(len(years))

        plt.figure(figsize=(12, 6))
        for i, region in enumerate(regions):
            plt.bar(x + i * bar_width, labor_force_data[region], width=bar_width, label=region)

        plt.title(" Labor force aged 15 and over by region (2011-2020)", fontsize=14)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Workforce 15+ (thousand people)", fontsize=12)
        plt.xticks(x + bar_width * (len(regions) / 2 - 0.5), years, fontsize=10)
        plt.legend(title="region", fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.6, axis='y')
        plt.tight_layout()
        group_bar_chart_path = os.path.join(output_folder, "labor_force_group_bar_chart.png")
        plt.savefig(group_bar_chart_path)
        plt.show()
        plt.close()

        # 2. Line chart to compare labor force across regions over time
        plt.figure(figsize=(12, 6))
        for region in regions:
            plt.plot(labor_force_data.index.astype(str), labor_force_data[region], label=region, marker='o')

        plt.title("Labor force aged 15 and over over the years by region (2011-2020)", fontsize=14)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Workforce 15+ (thousand people)", fontsize=12)
        plt.legend(title="region", fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        line_chart_path = os.path.join(output_folder, "labor_force_line_chart.png")
        plt.savefig(line_chart_path)
        plt.show()
        plt.close()

        # 3. Additional statistical analysis: Highest and lowest labor force per year
        for year in labor_force_data.index:
            max_region = labor_force_data.loc[year].idxmax()
            min_region = labor_force_data.loc[year].idxmin()
            print(f"Years {year}:")
            print(f"  - The region has the highest labor force: {max_region} with {labor_force_data.loc[year, max_region]} thousand people")
            print(f"  - Region with the lowest labor force: {min_region} with {labor_force_data.loc[year, min_region]} thousand people")
            print("-" * 50)

        print("Phân tích và lưu biểu đồ lực lượng lao động thành công!")

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")



# Example usage:
input_csv = 'data/cleaned/cleaned_population.csv'
output_folder = 'outputs/visualizations/Trend Analysis'

# Perform analysis
analyze_population_density(input_csv, output_folder)
analyze_average_population(input_csv, os.path.join(output_folder, "average_population.png"))
analyze_population_by_region(input_csv, output_folder)
analyze_natural_population_growth(input_csv, output_folder)
analyze_labor_force(input_csv, output_folder)
