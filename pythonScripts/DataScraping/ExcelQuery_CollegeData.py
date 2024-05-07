import pandas as pd

def excel_to_single_row(excel_file):
    df = pd.read_excel(excel_file)
    
    single_row = df.values.flatten()
    
    return single_row

def remove_blank_columns(df):
    non_blank_columns = df.iloc[1].notnull()
    df_filtered = df.loc[:, non_blank_columns]
    return df_filtered

def process_excel_to_csv_then_edit(excel_file, output_csv_file):
    excel_data = excel_to_single_row(excel_file)
    df = pd.DataFrame([excel_data])
    df.to_csv(output_csv_file, index=False)

    df = pd.read_csv(output_csv_file)
    
    df_filtered = remove_blank_columns(df)
    
    df_filtered.to_csv(output_csv_file, index=False)

def main():
    excel_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\UA_CDS.xlsx"  
    output_csv_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama_UniversityOfAlabama\new_output.csv"  
    process_excel_to_csv_then_edit(excel_file_path, output_csv_file)

main()

