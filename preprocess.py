import numpy as np
import pandas as pd
'''
Tiền Xử Lí Dữ Liệu
Sử dụng các kiến thức ở Lab1 để tiền xử lí dữ liệu như sau

    +Xóa các cột bị thiếu giá trị thuộc tính ở hơn 50% số mẫu
    +Điền các giá trị thiếu
    +Xóa các mẫu bị trùng lặp
    +Điền giá trị bị thiếu bằng mean ( cho thuộc tính numeric ) và mode cho thuộc tinh categorical
'''

df = pd.read_csv('hawks.csv')    # Đọc file hawks.csv
#df=df.drop_duplicates               # Xóa các dòng dữ liệu trùng ( ở file mẫu số dòng dữ liệu trùng là 0 )


df=df.replace(r'^\s*$', np.nan, regex=True) # Chuyển đổi các giá trị ' ' => NAN
#(df.isna().sum()*100/len(df) > 50 ) # Suy a các cột dữ liệu ReleaseTime Sex  Tarsus WingPitFat bị thiếu giá trị thuộc tính > 50 %
df.drop(columns=['ReleaseTime', 'Sex', 'Tarsus', 'WingPitFat'], inplace=True) #Xóa các cột bị thiếu giá trị thuộc tính ở hơn 50%
df.drop(columns=['BandNumber','CaptureTime'],inplace=True)  # Xoá cột dữ liệu Index & CaptureTime( Không có ý nghĩa đến thuộc tính lớp )

#df['CaptureTime'] = df['CaptureTime'].fillna(value=df['CaptureTime'].mode())

num_col = ['Wing', 'Weight', 'Culmen', 'Hallux', 'StandardTail', 'KeelFat', 'Crop']

for item in num_col:
    df[item] = df[item].fillna(df[item].mean())


setclass=['Month', 'Day', 'Year', 'Age', 'Wing',
       'Weight', 'Culmen', 'Hallux', 'Tail', 'StandardTail', 'KeelFat',
       'Crop','Species']

df = df.reindex(columns=setclass)

df1 = df.copy()

month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',  # Convert to Object
            6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
df1.Month = df1.Month.apply(lambda x: month[x])



day = {1: 'Week1', 2: 'Week1', 3: 'Week1', 4: 'Week1', 5: 'Week1',  # Convert to Object
            6: 'Week1', 7: 'Week1', 8: 'Week2', 9: 'Week2', 10: 'Week2', 11: 'Week2', 12: 'Week2',
            13: 'Week2', 14: 'Week2', 15: 'Week3', 16: 'Week3', 17: 'Week3', 18: 'Week3', 19: 'Week3',
            20: 'Week3', 21: 'Week3', 22: 'Week4', 23: 'Week4', 24: 'Week4', 25: 'Week4', 26: 'Week4',
            27: 'Week4', 28: 'Week4', 29: 'Week5', 30: 'Week5', 31: 'Week5'}
df1.Day = df1.Day.apply(lambda x: day[x])


year = {1992: 'Year-1992', 1993: 'Year-1993', 1994: 'Year-1994', 1995: 'Year-1995', 1996: 'Year-1996',  # Chuyển đổi giá trị Int Year -> object
            1997: 'Year-1997', 1998: 'Year-1998', 1999: 'Year-1999', 2000: 'Year-2000', 2001: 'Year-2001', 2002: 'Year-2002', 2003: 'Year-2003'}
df1.Year = df1.Year.apply(lambda x: year[x])


range = [37, 100, 200, 300,400,500]         # Rời rạc các giá trị Wing
grade_rank = pd.cut(df1['Wing'], range, right=False, labels=['0->100', '100->200', '200->300','300->400','400->500'])
df1['Wing'] = grade_rank


range = [0, 500, 1000, 1500,2000,2050]         #Rời rạc các giá trị Weight
grade_rank = pd.cut(df1['Weight'], range, right=False, labels=['0->500', '500->1000', '1000->1500','1500->2000','2000->2050'])
df1['Weight'] = grade_rank

range = [0, 10, 20, 30,40]         #Rời rạc các giá trị Culmen
grade_rank = pd.cut(df1['Culmen'], range, right=False, labels=['0->10', '10->20', '20->30','30->40'])
df1['Culmen'] = grade_rank


range = [0, 50, 100, 150, 200 , 250 , 300, 350]         #Rời rạc các giá trị Hallux
grade_rank = pd.cut(df1['Hallux'], range, right=False, labels=['0->50', '50->100', '100->150','150->200','200->250','250->300','300->350'])
df1['Hallux'] = grade_rank

range = [100, 150, 200 , 250 , 300]         #Rời rạc các giá trị Tail
grade_rank = pd.cut(df1['Tail'], range, right=False, labels=['100->150','150->200','200->250','250->300'])
df1['Tail'] = grade_rank

range = [100, 150, 200 , 250 , 300 , 350 ]         #Rời rạc các giá trị StandardTail
grade_rank = pd.cut(df1['StandardTail'], range, right=False, labels=['100->150','150->200','200->250','250->300','300->350'])
df1['StandardTail'] = grade_rank

range = [0, 1, 2 , 3 , 4.01 ]         #Rời rạc các giá trị KeelFat
grade_rank = pd.cut(df1['KeelFat'], range, right=False, labels=['0->1','1->2','2->3','3->4'])
df1['KeelFat'] = grade_rank


range = [0, 1, 2 , 3 , 4 , 5.01]         #Rời rạc các giá trị Crop
grade_rank = pd.cut(df1['Crop'], range, right=False, labels=['0->1','1->2','2->3','3->4','4->5'])
df1['Crop'] = grade_rank


df.to_csv('data.csv', header=True, index=False)
df1.to_csv('data1.csv', header=True, index=False)
#print(df.isnull().sum())  # Check dữ liệu sau khi tiền xử lí
print(df.dtypes)
print(df1.dtypes)