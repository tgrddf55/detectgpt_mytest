"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model import GPT2PPLV2 as GPT2PPL

# initialize the model
model = GPT2PPL()
import os

# 设置目录路径
directory = "human"

# 获取目录中的所有txt文件
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
retlist=[]
# 遍历所有txt文件并读取内容
i=0
for txt_file in txt_files:
    file_path = os.path.join(directory, txt_file)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            i+=1
            print(i,end="")
            ret=model(content,100,"v1.1")
            retlist.append(ret)
    except:
        pass

print(retlist)

#ret=model(sentence, 100, "v1.1")
#print(f'ret={ret}')
