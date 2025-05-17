import pandas as pd
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from idata import IData

class Data(IData):
    def __init__(self):
        try:
            scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('google-sheets-access/student-stress-457900-e232b54e76fb.json', scopes=scopes)

            self.client = gspread.authorize(creds)
            self.workbook = self.client.open("fontys_student_stress")
            self.sheet = self.workbook.worksheet('stress')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.sheet = None

    def get_data(self) -> pd.DataFrame:
        if self.sheet is None:
            raise RuntimeError("Google Sheet not loaded properly.")
        data = self.sheet.get_all_records()
        return pd.DataFrame(data)
    
