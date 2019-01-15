import os
import glob
import pandas as pd

df_keys = ["Order Date","Cust No", "Postcode", "Agent", "Order ref", "Order Source",
            "Disc Code", "Status", "Payment", "Item", "Description", "Qty", "Value net", 
            "P&P net", "Invoice Fee", "Total net", "Item Type", "Ship Date", "State", 
            "Delivery Date", "Carrier", "Tracking No"]

def get_dataframe(force):
    cur_dir = os.getcwd()
    #print(cur_dir)
    
    #df_total = pd.DataFrame()
    df_cur   = pd.DataFrame()
    df_acc   = pd.DataFrame()
    
    if force == True:
        if 'input' not in cur_dir:
            os.chdir('input')
            cur_dir = os.getcwd()
            print(f'Change to <{cur_dir}> directory')

        #print(f'Already into <{cur_dir}> directory')
        files_list = [str(f) for f in glob.glob("*.csv")]
        for file_str in files_list:
            print(f'Loading file <{file_str}>...')
            df_cur = pd.read_csv(file_str,skiprows=4, encoding='latin-1')
            df_cur = df_cur[df_keys]
            df_acc = df_acc.append(df_cur)            
            #print(df_acc['Order Date'].count())
            #print(df_total['Order Date'].count())

        #df_total = df_acc    
        #print(df_total['Order Date'].count())
        print('Datafram generated')
        os.chdir('../')  
        df_acc.to_csv("output/main_dataframe.csv", encoding='utf-8', index=False)
    else:
        print(f'Loading from file <output/main_dataframe.csv>...')
        try:
            df_acc = pd.read_csv("output/main_dataframe.csv", encoding='latin-1')
        except :
            print('Error: file <output/main_dataframe.csv> not found')
        print('Dataframe generated')
        
    return df_acc                 
                      
#get_dataframe(False)            