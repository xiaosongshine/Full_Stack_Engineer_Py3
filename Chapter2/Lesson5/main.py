#python3
"""
统计《西游记》中：
共出现了多少个不同的汉字；
每个汉字出现了多少次；
出现得最频繁的汉字有哪些。
"""

#Windows 运行，打开方式要用utf8，不然会出错
fr = open('xyj.txt', 'r', encoding="utf8")##（Py2）fr = open('xyj.txt', 'r')

characters = []
stat = {}

for line in fr:
	# 去掉每一行两边的空白
	line = line.strip()
	# 如果为空行则跳过该轮循环
	if len(line) == 0:
		continue
	# 将文本转为unicode，便于处理汉字
	#line = unicode(line)#因为打开方式为utf8
	# 遍历该行的每一个字
	for x in range(0, len(line)):
		# 去掉标点符号和空白符
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未记录在characters中
		if not line[x] in characters:
			characters.append(line[x])
		# 尚未记录在stat中
		if line[x] not in stat: ## (Py2)if not stat.has_key(line[x]):
			stat[line[x]] = 0
		# 汉字出现次数加1
		stat[line[x]] += 1
print("共有汉字个数：")
print(len(characters))
print("共有字典个数：")
print(len(stat))



# lambda生成一个临时函数
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
statList = sorted(stat.items(), key=lambda d:d[1], reverse=True)


fw = open('result.csv', 'w', encoding="utf8")##（Py2）fw = open('result.csv', 'w')
for item in statList:
	# 进行字符串拼接之前，需要将int转为str
	fw.write(item[0] + ',' + str(item[1]) + '\n')
fw.close()

print("输出出现频率最大的十个字和出现的次数")
for t in range(0,10):
    print("汉字："+(statList[t][0])+" 出现次数："+str(statList[t][1]))

fr.close()
