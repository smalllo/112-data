#109021049-羅浩維
#1
squares_dict = {}# 創建一個空的字典來存儲結果
for i in range(10):
    squares_dict[i] = i * i# 將數字i的平方添加到字典中
print(squares_dict)# 輸出字典，顯示數字和它們的平方
#2
ascii_dict = {}
for letter in 'abcdefghijklmnopqrstuvwxyz':# 創建一個空的字典來存儲結果
    ascii_dict[letter] = ord(letter)# 將字母轉換成它們的ASCII碼並添加到字典中
print(ascii_dict)# 輸出字典，顯示字母和它們的ASCII碼
