import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet:
    def __init__(self,jsonName='',DriveAccount=''):
        self.DriveAccount=DriveAccount
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(jsonName, scope)
        self.client = gspread.authorize(creds)
        
    def checkExist(self,FileName):
        titles_list = []
        for spreadsheet in self.client.openall():
            titles_list.append(spreadsheet.title)
        print(titles_list)
        if FileName not in titles_list:
            return False
        else:
            return True   

    def delWorksheet(self,FileName):
        if(self.checkExist(FileName)):
            sh = self.client.open(FileName)
            self.client.del_spreadsheet(sh.id)
            return None
        else:
            return None
    
    def createNew(self,FileName):
        if(checkExist(FileName)):
            return "File already exists"
        else:
            try:
                sh = self.client.create(FileName)
                sh.share(self.DriveAccount, perm_type='user', role='writer')
                print("File "+FileName+" created and shared to "+self.DriveAccount)
            except:
                return "File can not be created"

    def openFile(self,Name):
        if(checkExist(FileName)):
            try:
                sheet = self.client.open(Name).sheet1
                return sheet
            except:
                return "File failed to open"
        else:
            return "File doesnt exist"

