t = 68
lines_to_write = []  # 用于暂时存储要写入文件的行
lines_count = 0  # 计数器，用来记录每5行

with open('a.txt', 'r', encoding='utf-8') as infile:
    # 逐行处理文件
    for i, line in enumerate(infile, start=1):
        # 去除行两端的空格和换行符
        line = line.strip()
        # 如果该行既不是数字，也不是空行
        if not line.isdigit() and line != "":
            lines_to_write.append(line)
            lines_count += 1

            # 每5行写入一个新文件
            if lines_count == 5:
                t += 1
                with open(f'{t}.txt', 'w', encoding='utf-8') as outfile:
                    outfile.write("\n".join(lines_to_write))  # 将5行写入文件
                lines_to_write.clear()  # 清空暂存的行
                lines_count = 0  # 重置计数器

# 处理剩余不足5行的情况
if lines_to_write:
    t += 1
    with open(f'{t}.txt', 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(lines_to_write))  # 写入剩余的行
