import pandas as pd

def excel_to_single_row(excel_file):
    df = pd.read_excel(excel_file)
    
    single_row = df.values.flatten()
    
    return single_row

def write_to_csv(data, output_file):
    df = pd.DataFrame([data])
    
    df.to_csv(output_file, index=False)

def remove_blank_columns(df):
    non_blank_columns = df.iloc[1].notnull()
    df_filtered = df.loc[:, non_blank_columns]
    return df_filtered

def process_csv(input_file, output_file):
    df = pd.read_csv(input_file, header=None)
    
    df_filtered = remove_blank_columns(df)
    
    df_filtered.to_csv(output_file, index=False, header=False)

def main():
    excel_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\UA_CDS.xlsx"  # Provide the path to your Excel file
    output_csv_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\new_output.csv"  # Specify the path for the output CSV file
    
    row_data = excel_to_single_row(excel_file_path)
    write_to_csv(row_data, output_csv_file)

    new_input_csv_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\new_output.csv"  # Specify the path to your input CSV file
    new_output_csv_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\dat_new_new_output.csv"  # Specify the path for the output CSV file
    
    process_csv(new_input_csv_file, new_output_csv_file)

main()