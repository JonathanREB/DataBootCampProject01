import os
import glob
import pandas as pd

df_keys = ["Order Date","Cust No", "Postcode", "Agent", "Order ref", "Order Source",
            "Disc Code", "Status", "Payment", "Item", "Description", "Qty", "Value net", 
            "P&P net", "Invoice Fee", "Total net", "Item Type", "Ship Date", "State", 
            "Delivery Date", "Carrier", "Tracking No"]

def load_files():
    cur_dir = os.getcwd()
    #print(cur_dir)
    
    #df_total = pd.DataFrame()
    df_cur   = pd.DataFrame()
    df_acc   = pd.DataFrame()
    
    if 'input' not in cur_dir:
        os.chdir('input')
        cur_dir = os.getcwd()
        print(f'Change to <{cur_dir}> directory')

    print(f'Already into <{cur_dir}> directory')
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
    os.chdir('../')    
    return df_acc                 
                      
#load_files()            
            
#files = []
#files = os.listdir()