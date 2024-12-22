import csv

# 打开txt文件读取数据
with open('human_result.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# 创建并写入CSV文件
with open('human_result.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # 写入表头
    writer.writerow(["Text", "Label"])

    # 处理每一行
    for line in lines:
        line = line.strip()  # 去掉行首尾空白字符
        label = "Human" if "Human" in line else "AI"  # 判断标签
        writer.writerow([line, label])  # 写入到CSV文件
