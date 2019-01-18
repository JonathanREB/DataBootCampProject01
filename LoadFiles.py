import os
import glob
import pandas as pd
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

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
        if len(files_list) > 0:
            for file_str in files_list:
                print(f'Loading file <{file_str}>...')
                df_cur = pd.read_csv(file_str,skiprows=4, encoding='latin-1')
                df_cur = df_cur[df_keys]
                df_acc = df_acc.append(df_cur)            
                #print(df_acc['Order Date'].count())
                #print(df_total['Order Date'].count())

            #df_total = df_acc    
            #print(df_total['Order Date'].count())
            
            df_acc['State'] = df_acc['State'].replace(['AGS', 'AGS.', 'AGUAS CALIENTES', 'AGUASCALIENTES', 'Ags.','Aguascalientes'],'AGUASCALIENTES')
            df_acc['State'] = df_acc['State'].replace(['MÃ\x89XICO', 'MÃ©xico', 'MEX', 'MEXECO','ESTADO DE MEX', 'EDO DE MEX', 'EDO DE MEXICO', 'EDO MEX', 'EDO. MEXICO', 'EDO.MEX.', 'EDO.MEXICO', 'EDO.NEX.', 'EDOMEX', 'EDOMEX.', 'ESATADO DE MEXICO', 'ESATDO DE MEXICO', 'ESTADO DE MEXICO', 'ESTADO DE MÃ\x89XICO', 'Edomex.'],'MEXICO')
            df_acc['State'] = df_acc['State'].replace(['TIJUANA', 'B.C', 'B.C.', 'B.C. NORTE', 'B.C.S.', 'B.C.S. SUR', 'BAJA CALIFORNIA', 'BAJA CALIFORNIA NORTE', 'BAJA CALIFORNIA SUR', 'BAJA CALIFORNNIA SUR', 'BAJA NCALIFORNIA SUR', 'BAJACALIFORNIA', 'BAJACALIFORNIA SUR', 'BCN', 'BCS', 'Baja California', 'Baja California Sur'],'BAJACALIFORNIA')
            df_acc['State'] = df_acc['State'].replace(['CIUDAD DE MEXICO', 'CIUDAD DE MÃ\x89XICO', 'CUIDAD DE MEXICO', 'Ciudad de MÃ©xico', 'D.F', 'D.F.', 'DE MEXICO', 'DF', 'DIF', 'DISTRITO', 'DISTRITO FEDERAL', 'DISTRITO FEERAL', 'DISTRITO FERDERAL', 'Distrito Federal'],'CDMX')
            df_acc['State'] = df_acc['State'].replace(['ZAC', 'ZAC.', 'ZACATECAS', 'ZACATECAZ', 'ZEMPOALA VERACRUZ', 'Zac.', 'Zacatecas'],'ZACATECAS')
            df_acc['State'] = df_acc['State'].replace(['SIGUATANEJO', 'ACAPULCO GUERRERO', 'GERRERO', 'GRO', 'GRO.', 'GTO', 'GTO.', 'GUERREO', 'GUERRERO', 'Gro.', 'Guerrero'],'GUERRERO')
            df_acc['State'] = df_acc['State'].replace(['PUE', 'PUE.', 'PUEBLA', 'Pue.', 'Puebla'], 'PUEBLA')
            df_acc['State'] = df_acc['State'].replace(['QRO', 'QUE' ,'QUERETARO', 'QUERÃ\x89TARO', 'Qro.', 'QuerÃ©taro','QRO.'], 'QUERETARO')
            df_acc['State'] = df_acc['State'].replace(['Camp.', 'Campeche','CAM','CAMP.','CAMPECHE'], 'CAMPECHE')
            df_acc['State'] = df_acc['State'].replace(['Q.ROO.', 'Q.Roo.', 'CANCUN','CANCUN QUINTANA ROO','CANCUN QUINTANAROO','QUINTA ROO','QUINTANA ROO','Quintana Roo', 'ROO', 'QUINTANARRO'], 'QUINTANA ROO')
            df_acc['State'] = df_acc['State'].replace(['ORIZABA VERACRUZ', 'POZA RICA', 'VER','VER.', 'VERACRUZ','VERACRUZ DE IGNACIO DE LA LLAVE', 'Ver.', 'Veracruz','Veracruz de Ignacio de la Llave', 'Veracruz de Ignacio de la Llavev'], 'VERACRUZ')
            df_acc['State'] = df_acc['State'].replace(['JAL', 'JAL.', 'JALICO', 'JALISCO', 'Jal.', 'Jalisco', 'GUA', 'GUADALAJARA',], 'JALISCO')
            df_acc['State'] = df_acc['State'].replace(['MERIDA', 'YUC', 'YUC.', 'YUCATÃ\x81N', 'Yuc.', 'YucatÃ¡n'], 'YUCATAN')
            df_acc['State'] = df_acc['State'].replace(['S.L.P.', 'San Luis PotosÃ\xad', 'SLP', 'SAN LUIS DE LA PAZ', 'SAN LUIS POTOSI', 'SAN LUIS POTOSÃ\x8d'], 'SAN LUIS POTOSI')
            df_acc['State'] = df_acc['State'].replace(['DGO.', 'DUR', 'DURANFO', 'DURANGO', 'Dgo.', 'Durango'], 'DURANGO')
            df_acc['State'] = df_acc['State'].replace(['MichoacÃ¡n de Ocampo','MUCHOACAN', 'Mich.', 'MichoacÃ¡n', 'MichoacÃ¡n de Ocampo' 'Mor.','MOR', 'MOR.', 'MORELIA' ,'MIC', 'MICH.', 'MICHIOACAN', 'MICHOACAN', 'MICHOACÃ\x81N DE OCAMPO', 'MICHOCAN'], 'MICHOACAN') 
            df_acc['State'] = df_acc['State'].replace(['CELAYA',  'Gto.', 'Guanajuato'], 'GUANAJUATO')
            df_acc['State'] = df_acc['State'].replace(['CHP', 'CHH', 'CHIAPAS', 'CHIH.','CHIS.', 'Chis.', 'Chiapas'], 'CHIAPAS')
            df_acc['State'] = df_acc['State'].replace(['SALTILLO', 'Coah.', 'Coahuila', 'Coahuila de Zaragoza', 'CUAHUILA', 'COHAULA', 'COA', 'COAH.', 'COAHUILA', 'COAHUILA DE ZARAGOZA', 'COHAHUILA', 'COHAULA'], 'COAHUILA')
            df_acc['State'] = df_acc['State'].replace(['COL', 'COLIMA','Col.', 'Colima'], 'COLIMA')
            df_acc['State'] = df_acc['State'].replace(['morelos', 'CUERNAVACA', 'MORELOS', 'Mor.', 'Morelos'], 'MORELOS')
            df_acc['State'] = df_acc['State'].replace(['MONTERREY', 'MONTERREY NUEVO LEON', 'Nuevo LeÃ³n', 'LEON', 'N.L', 'N.L.', 'NLE', 'NUEVO LEON', 'NUEVO LEÃ\x93N', 'NUEVOLEON', 'Nuevo LeÃ³n'], 'NUEVO LEON')
            df_acc['State'] = df_acc['State'].replace(['OAX', 'OAX.', 'OAXACA', 'OXACA', 'Oax.', 'Oaxaca'], 'OAXACA')
            df_acc['State'] = df_acc['State'].replace(['JUAREZ', 'CHIHUAHUA', 'CHIUAHUA','Chih.', 'Chihuahua'], 'CHIUAHUA')
            df_acc['State'] = df_acc['State'].replace(['HGO.', 'HID', 'HIDALGO', 'Hgo.', 'Hidalgo'], 'HIDALGO')
            df_acc['State'] = df_acc['State'].replace(['Son.', 'Sonora','HERMOSILLO SONORA','SON', 'SON.', 'SONORA'], 'SONORA')
            df_acc['State'] = df_acc['State'].replace(['NAY', 'NAYARIT', 'Nay.', 'Nayarit'], 'NAYARIT')
            df_acc['State'] = df_acc['State'].replace(['Tab.', 'Tabasco', 'TAB', 'TAB.', 'TABASCO'], 'TABASCO')
            df_acc['State'] = df_acc['State'].replace(['CULIACAN', 'SIN', 'SIN.', 'SINALOA', 'Sin.', 'Sinaloa'], 'SINALOA')
            df_acc['State'] = df_acc['State'].replace(['TLA', 'TLAX.', 'TLAXCALA', 'Tlax.', 'Tlaxcala'], 'TLAXCALA')
            df_acc['State'] = df_acc['State'].replace(['TAM', 'TAMAULIPAS', 'TAMPICO', 'TAMPS.', 'Tamaulipas', 'Tamps.'], 'TAMAULIPAS')
            
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


def get_chart(data_frame, combo_box):
    #ip = widgets.FloatProgress(min=0,max=100)
    #display(ip)

    index = 0
    list_order_status_tmp = [] #list_order_status
    list_groupby = ['MonthYear','Year','Status']

    df_orders_month_status = data_frame
    list_cb = combo_box
    
    df_orders_month_status = df_orders_sum.groupby(list_groupby, as_index=False).count()
    list_groupby.append('Order Date')
    df_orders_month_status = df_orders_month_status[list_groupby]
    df_orders_month_status = df_orders_month_status.rename(columns={'Order Date' : 'Nbr of orders'})

    for cb in list_cb:
        if cb.value != False:
            #print(cb.description)
            list_order_status_tmp.append(cb.description) 
        index += 1   

    ip.value = 25
    #print(list_order_status_tmp)
    list_order_status = list_order_status_tmp
    #print(list_order_status)

    test = "item_tmp2['Year'] == '2018'"

    list_os = []
    for status in list_order_status:
        #print(status)
        item_tmp = df_orders_month_status.loc[df_orders_month_status['Status'] == status]
        #item_tmp = item_tmp2.loc[item_tmp2['Year'] == '2018']    
        list_os.append(item_tmp)    
    #print(list_os)    

    plt.close()
    plt.figure(figsize=(25,10))
    plt.rcParams.update({'font.size': 14})      

    flt = list_groupby[0]

    progress = len(list_os[1].count())
    progress_step = 100 / progress
    cont = 0

    ip.value = 50
    #plt.plot(df_orders_month_status_all['MonthYear'], df_orders_month_status_all['Nbr of orders'] , color='r')
    #plt.legend('All')#list_os[cont]['Status'])

    for item in list_os:
        plt.plot(list_os[cont][flt], list_os[cont]['Nbr of orders'], label =list_os[cont]['Status'] )#, color='r')
        #plt.legend(list_order_status)#list_os[cont]['Status'])    
        #if cont == 0:    
        #print(list_os[cont][flt])
        ip.value += progress_step
        cont +=1   

    plt.plot(df_orders_month_status_all['MonthYear'], df_orders_month_status_all['Nbr of orders'] , color='k')
    list_order_status.append('Total Orders')
    plt.legend(list_order_status)#list_os[cont]['Status'])

    if (cb_save.value == True):    
        plt.savefig('chart.jpg')

    plt.show()    

    #item_tmp.head()    


    list_order_status = df_orders_sum['Status'].unique()        
    

#get_dataframe(True)            