#109021049-羅浩維
#1
result_list_1 = []  # 創建一個空的列表來存儲結果
for i in range(10, 56, 5):  # 從10開始，每次增加5，直到55 (不包含)
    result_list_1.append(i)  # 將每個數字添加到列表中
print(result_list_1)  # 輸出列表

#2
result_list_2 = []  # 創建一個空的列表來存儲結果
value = 3  # 初始值設定為3
for _ in range(9):  # 重複9次
    result_list_2.append(value)  # 將目前的值添加到列表中
    value *= 2  # 將目前的值乘以2
print(result_list_2)  # 輸出列表

#3
result_list_3 = []  # 創建一個空的列表來存儲結果
for i in range(1, 6):  # 從1到5 (包含)
    result_list_3.extend([i] * i)  # 將i重複i次，然後添加到列表中
print(result_list_3)  # 輸出列表

#4
result_list_4 = []  # 創建一個空的列表來存儲結果
for i in range(1, 7):  # 從1到6 (包含)
    result_list_4.append(chr(96 + i) * i)  # 添加字母，次數為i
print(result_list_4)  # 輸出列表

#5
result_list_5 = []  # 創建一個空的列表來存儲結果
for i in range(11):  # 從0到10 (包含)
    if i == 0:
        result_list_5.append(i)  # 如果i等於0，只添加一次0到列表中
    else:
        result_list_5.extend([i, -i])  # 否則添加i和-i到列表中
print(result_list_5)  # 輸出列表




