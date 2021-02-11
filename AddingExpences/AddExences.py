import datetime
import pandas as pd

class AddingExpence:
    def Income(self,df,cat,value,date=datetime.datetime.now().strftime("%x"),note=""):
        if(value > 0):
            d = {'Catorgary': [cat], 'Value': [value], 'Date' : [date], 'Note' : [note]}
            df2 = pd.DataFrame(data=d)
            df.append(df2)
            return df
        elif(value < 0):
            d = {'Catorgary': [cat], 'Value': [-value], 'Date' : [date], 'Note' : [note]}
            df2 = pd.DataFrame(data=d)
            df.append(df2)
            return df
        else:
            print("Inputed cost is 0")
            return df

    def Outgoing(self,cat,value,date=datetime.datetime.now().strftime("%x"),note=""):
        if(value > 0):
            d = {'Catorgary': [cat], 'Value': [-value], 'Date' : [date], 'Note' : [note]}
            df2 = pd.DataFrame(data=d)
            df.append(df2)
            return df
        elif(value < 0):
            d = {'Catorgary': [cat], 'Value': [value], 'Date' : [date], 'Note' : [note]}
            df2 = pd.DataFrame(data=d)
            df.append(df2)
            return df
        else:
            print("Inputed cost is 0")
            return df

