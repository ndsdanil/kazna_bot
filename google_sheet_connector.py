import gspread
from oauth2client.service_account import ServiceAccountCredentials

class google_sheet_connector:
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    #'kazna' file bellow located in git ignore(kazna is my virtual environment file) json file bellow you can generate using google API for Google Sheet. Use this video to generate json: https://www.youtube.com/watch?v=w533wJuilao 
    creds = ServiceAccountCredentials.from_json_keyfile_name("kazna\kazna_GS_Cred.json",scope)
    client = gspread.authorize(creds)

    #variablse related with the methadata
    collumns_dict = {'date_cell':'A', 'number_cell':'B', 'income_or_expense_cell':'C', 'from_to_cell':'D'}
    money_storage_dict = {'cash euro with me':'E', 'cash euro not with me':'F', 'cash $ with me':'G', 'cash $ not with me':'H', 'card euro':'I', 'card $':'J', 'cash (RUB) not with me':'K', 'card (RUB)':'L', 'bitcoin':'M', 'shares(RUB)':'N'}
    money_storage_info_list = []

    def get_sheet_connector():
        #return sheet connection
        sheet = google_sheet_connector.client.open("kazna").sheet1
        return sheet
    
    def set_values_in_sheet(self, list):    
        sheet = google_sheet_connector.get_sheet_connector()
        column_letter = '1'
        column_values = len(sheet.col_values(column_letter))+1
        i = 0
        for val in self.collumns_dict.values():
            cell = val + str(column_values)
            sheet.update_acell(cell, list[i])
            i = i + 1
        i = 0
        for key, val in self.money_storage_dict.items():
            cell1 = val + str(column_values - 1)
            cell2 = val + str(column_values)
            value = sheet.get_values(cell1)[0][0]
            sheet.update_acell(cell2, value)
    
            if key == list[4]:
                if list[1] == 'Income':
                    value = float(value) + float(list[2])
                    sheet.update_acell(cell2, value)
                if list[1] == 'Expense':
                    value = float(value) - float(list[2])
                    sheet.update_acell(cell2, value)
                

        


#Here we can check the connection
#print(sheet.get_all_records())
