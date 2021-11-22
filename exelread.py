import pandas as pd
 
df = pd.read_excel('Templog.xlsx')

data_ondo = df[df['B00'].str.contains('℃', na=False)]
data_volt = df[df['B00'].str.contains('V', na=False)]
data_ohm = df[df['B00'].str.contains('Ω', na=False)]
writer = pd.ExcelWriter('Temp抽出後.xlsx', engine= 'xlsxwriter')

data_ondo.to_excel(writer, sheet_name = '温度', index=False)
data_volt.to_excel(writer, sheet_name = '電圧', index=False)
data_ohm.to_excel(writer, sheet_name = '抵抗値', index=False)

writer.save()
writer.close()

print('文字列：書き込み終了')