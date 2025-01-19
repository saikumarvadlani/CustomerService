import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def create_bar_graph(input_file_path, output_file_path, image_file_path):

    try:
        # Step 1: Load the Excel file
        sheet_name = 'Sheet1' 
        df = pd.read_excel(input_file_path, sheet_name=sheet_name)

        # Step 2: Group and count unique values in the column
        column_name = "Issue_Category" 
        if column_name not in df.columns:
            return f"Error: Column '{column_name}' not found in the Excel file."

        value_counts = df[column_name].value_counts()

        # Step 3: Create and save the bar graph
        plt.figure(figsize=(8, 5))
        plt.bar(value_counts.index, value_counts.values, color='skyblue')
        plt.xlabel('Issue Category', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.title('Betsson Group Customer Service', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(image_file_path)
        plt.close()

        # Step 4: Insert the graph into the Excel file
        wb = load_workbook(input_file_path)
        ws = wb[sheet_name]
        img = Image(image_file_path)
        img.anchor = 'I5'  
        ws.add_image(img)

        # Save the updated Excel file
        wb.save(output_file_path)
        return f"Succ}'."

    except FileNotFoundError:
        return f"Err"
    except ValueError as ve:
        return f"Value Error: {ve}"
    except Exception as e:
        return f"An : {e}"

