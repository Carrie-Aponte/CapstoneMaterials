import pdfquery
import pandas as pd
import os

filename = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama\UniversityOfAlabama\UA_CDS 2022-23 FINAL.pdf"
output_filename = r"C:\Users\carrie\Documents\CIS_598_Capstone\Additional_Research_Files\Alabama\UniversityOfAlabama"

try:
    pdf = pdfquery.PDFQuery(filename)

    pdf.load()

    xpath_queries = {
        #'CollegeName': '//text()[contains(., "Name of College/University:")]'
        'CollegeName': '//LTTextLineHorizontal[contains(., "Name of College/University:")]'
        #'State': '//text()[contains(., "City/State/Zip/Country")]/following-sibling::text()[1]',
        #'Enrollment': '//text()[contains(., "Total all undergraduates")]/following-sibling::text()[1]',
        #'GraduationRate': '//text()[contains(., "Graduation rate")]/following-sibling::text()[1]',
        #'AnnualExpenses': '//text()[contains(., "Public institutions in-state")]/following-sibling::text()[1]',
        #'FinancialAid': '//text()[contains(., "Total Scholarships/Grants")]/following-sibling::text()[1]'

    }

    extracted_data = {}
    for field_name, xpath_query in xpath_queries.items():
        data = pdf.pq(xpath_query)
        extracted_data[field_name] = [element.text.strip() for element in data]
        print("Extracted data for {}: {}".format(field_name, extracted_data[field_name]))

    
    #data_list = [element.text.strip() for element in data]

    #num_columns = 6
    num_columns = 1
    df = pd.DataFrame(extracted_data)
    #df.columns = ['CollegeName','State','Enrollment', 'GraduationRate','AnnualExpenses', 'FinancialAid']
    df.columns = ['CollegeName']
    output_filename = os.path.splittext(filename)[0] + ".xlsx"
    df.to_excel((output_filename), index=False)
except Exception as e:
    print("Error processing file {}: {}".format(filename, e))