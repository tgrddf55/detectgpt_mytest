'''
for i in range(41, 101):
    with open(f"{i}.txt", "w") as file:
        pass  # Create an empty file'''
t=71
with open('a.txt', 'r', encoding='utf-8') as infile:
    # 逐行处理文件
    for i, line in enumerate(infile, start=1):
        # 去除行两端的空格和换行符
        line = line.strip()
        # 如果该行既不是数字，也不是空行
        if not line.isdigit() and line != "":
            t+=1
            # 以行号为文件名写入内容
            with open(f'{t}.txt', 'w', encoding='utf-8') as outfile:
                outfile.write(line)