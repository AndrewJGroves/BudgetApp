import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet:

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    # This links to the credentials that we ahve generated
    creds = ServiceAccountCredentials.from_json_keyfile_name(jsonName, scope)
    client = gspread.authorize(creds)

    def __init__(self,jsonName,DriveAccount):
        self.jsonName=jsonName
        self.DriveAccount=DriveAccount

    def createNew(self,FileName)
        try:
            sh = gc.create(FileName)
            sh.share(self.DriveAccount, perm_type='user', role='writer')
        except:
            raise ValueError("File can not be created")

    def openFile(self,Name)
        try:
            sheet = client.open(Name).sheet1
            return sheet
        except:
            raise ValueError("File failed to open")



