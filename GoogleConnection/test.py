import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# This links the 2 apis we are using
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# This links to the credentials that we ahve generated
creds = ServiceAccountCredentials.from_json_keyfile_name('link.json', scope)
client = gspread.authorize(creds)

#Opens the sheet, need to be share with the email from link.json
sheet = client.open('Test').sheet1

#Updates a cell 
sheet.update_cell(3,3,'test')

#Gets the values of a row
sheet.row_values(1)

#Gets all the values
sheet.get_all_values()

