# pandas 入门
# pandas 主要数据结构为一维数据和dataframe（二维数据）
# Pandas 主要引入了两种新的数据结构：DataFrame 和 Series。
# Series： 类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成。
# DataFrame： 类似于一个二维表格，DataFrame 可视为由多个 Series 组成的数据结构：
import pandas as pd
import numpy as np
pd.__version__  # 查看pandas的版本


mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

type(mydataset) #创建一个字典

myvar = pd.DataFrame(mydataset) # 转换为数据框
type(myvar)
print(myvar)



# Pandas Series ,类似于 Python 中的列表,标签（索引）
# 字典、数组、列表都可以创建series

a_list = [12,34,46,12,43,12]
a_series = pd.Series(a_list)

b_tuple = ('a','as','df','ss','aq','we')

b_series = pd.Series(b_tuple)

b_series[1] # 索引

c_series = pd.Series(a_list,index = b_tuple) # index指定索引
print(c_series)
c_series['as']  # 根据索引取出数据
c_series[2]  # 索引为2的值
c_series[1:3]
c_series[:3]
c_series['as':'ss']








d_series = pd.Series(a_list,index = b_tuple,name = 'A series')
print(d_series)

# 用字典创建series
e_dict = {'sd': "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(e_dict)

print(myvar)

# 使用 NumPy 数组创建 Series
array_series = pd.Series(np.array([1, 2, 3, 4]))
array_series
# 为特定的索引标签赋值
array_series[2] = 23
array_series

# 通过赋值给新的索引标签来添加元素
array_series['e'] = 5 

# 使用 del 删除指定索引标签的元素
del array_series[3]


# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。

a_new_series = array_series.drop([2])
a_new_series


# 算术运算
series_1 = pd.Series([23,11,12,34,45,42])
sum_2 = series_1 * 2
sum_2

# 过滤
filtered_series = series_1[series_1 > 20]  # 选择大于2的元素
filtered_series

# 数学函数
series_sqrt = np.sqrt(series_1)  # 对每个元素取平方根
series_sqrt

# 用 Series 的方法来计算描述性统计。
s = pd.Series([23,1,21,23,4,5,5,66,44,232,212,34])
print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差

# 获取索引
index = s.index
index

# 获取值数组
values = s.values
values

# 获取描述统计信息
stats = s.describe()
stats

# 其他属性和方法
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个

# 使用布尔表达式：根据条件过滤 Series。

print(s > 200)  # 返回一个布尔 Series，其中的元素值大于 2

# 转换数据类型：使用 astype 方法将 Series 转换为另一种数据类型。

s_1 = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型
s_1



# DataFrame 是 Pandas 中的另一个核心数据结构
# 可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象

# 创建列表
data_1 = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
data_1 

dataframe_1 = pd.DataFrame(data_1, columns=['Site', 'Age'])
dataframe_1

# 使用astype方法设置每列的数据类型
dataframe_1['Site'] = dataframe_1['Site'].astype(str)
dataframe_1['Age'] = dataframe_1['Age'].astype(float)

# 字典创建数据框
data_2 = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

dataframe_2 = pd.DataFrame(data_2,index = ('as','sd','df'))
print (dataframe_2)

# 创建一个包含网站和年龄的二维ndarray
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])

# 使用DataFrame构造函数创建数据帧
dataframe_3 = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
# 打印数据帧
print(dataframe_3)


# 实例 - 使用字典创建
data_3 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
data_3
dataframe_4 = pd.DataFrame(data_3)

print (dataframe_4)


# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1


data_4 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
dataframe_5 = pd.DataFrame(data_4,index = ('x','y','z'))
dataframe_5
# 返回第一行
print(dataframe_5.loc['x'])
# 返回第二行
print(dataframe_5.loc['z'])

# 返回多行数据
print(dataframe_5.loc[['x', 'y']])

# 字典的键成为列名，值成为列数据
# 通过字典创建 DataFrame
df_1 = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
df_1

# 从 NumPy 数组创建：提供一个二维 NumPy 数组。

# 通过 NumPy 数组创建 DataFrame
df_2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
df_2

# 从 Series 创建 DataFrame：通过 pd.Series() 创建。
# 从 Series 创建 DataFrame
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df_3 = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
df_3

# DataFrame 的属性和方法
print(df_3.shape)     # 形状
print(df_3.columns)   # 列名
print(df_3.index)     # 索引
print(df_3.head())    # 前几行数据，默认是前 5 行
print(df_3.tail())    # 后几行数据，默认是后 5 行
print(df_3.info())    # 数据信息
print(df_3.describe())# 描述统计信息
print(df_2.mean())    # 求平均值
print(df_3.sum())     # 求和


# 访问 DataFrame 元素
df_3

## 访问列
# 通过列名访问
print(df_3['Name'])


# 通过属性访问
print(df_3.City)   

# 通过 .loc[] 访问
print(df_3.loc[:, 'Age'])

# 通过 .iloc[] 访问
print(df_3.iloc[:, 1])  # 'Age' 是第2列

# 访问单个元素
print(df_3['Name'][0])  # 访问Name列，第一行元素

## 访问行
# 通过行标签访问
print(df_3.loc[0])


# 修改 DataFrame

df_3['Age'] = [10, 11, 12]
df_3

# 添加新列：给新列赋值。
df_3['NewColumn'] = [100, 200, 300]
df_3


# 添加新行：使用 loc、concat 方法。
# 使用 loc 为特定索引添加新行
df_3.loc['sd'] = [13, 14, 15, 16]
df_3

# 使用concat添加新行
new_row = pd.DataFrame([[4, 7]], columns=['A', 'B'])  # 创建一个只包含新行的DataFrame
new_row
df_4 = pd.concat([df_3, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
print(df_4)



df_5 = pd.DataFrame({'name':['a','b','c','d','e'],
                     'age' :[12,13,12,11,12],
                     'grade':[2,4,2,2,3]})

df_5

# 删除 DataFrame 元素

# 删除列：使用 drop 方法。
df_dropped_c = df_5.drop('grade',axis = 1)

df_dropped_c

# 删除行：同样使用 drop 方法。

df_dropped_r = df_5.drop(0)  # 删除索引为 0 的行
df_dropped_r

# DataFrame 的统计分析
df_5
df_5.describe()

df_5['age'].sum()
df_5['grade'].mean()

df_5['age'].max()
df_5['grade'].min()

# DataFrame 的索引操作
df_6 = pd.DataFrame({'name':['da','bd','cs','ds','se'],
                     'age' :[12,13,12,11,12],
                     'grade':[2,5,2,3,3],
                     'result':[67,132,89,123,135]})
df_6

# 重置索引：使用 .reset_index()。

df_reset = df_6.reset_index(drop=True)
df_reset

# 设置索引：使用 .set_index()。


df_set = df_6.set_index('age') # 将age列设置为索引
df_set 


# DataFrame 的布尔索引

# 使用布尔表达式：根据条件过滤 DataFrame。

df_6[df_6['result'] > 80]

# DataFrame 的数据类型

# 查看数据类型：使用 dtypes 属性。

df_6.dtypes

# 转换数据类型：使用 astype 方法。

df_6['name'] = df_6['name'].astype('str')


# DataFrame 的合并与分割

# 合并：使用 concat 或 merge 方法。

df_7 = pd.DataFrame({'name':['da','bd','cs','ds','se'],
                     'age' :[12,13,12,11,12],
                     'grade':[2,5,2,3,3],
                     'result':[67,132,89,123,135]})
df_8 = pd.DataFrame({'name':['da','bd','cs','ds','se'],
                     'city':['da','bd','cs','ds','se'],
                     'sex' :[1,2,1,1,2]})
df_9 = pd.DataFrame({'name':['erf'],
                     'age' :[15],
                     'grade':[6],
                     'result':[32],
                     'city':['df'],
                     'sex' :[1]})
df_7
df_8
df_9


# 横向合并,merge有一列相同
pd_merge = pd.merge(df_7,df_8, on='name')
pd_merge
# 纵向合并
pd.concat([pd_merge, df_9], ignore_index=True)


# 分割：使用 pivot、melt 或自定义函数。

# 长格式转宽格式

df_10 = pd.DataFrame({'age' :[12,13,14,15,16,12,13,14,15,16,12,13,14,15,16],
                      'grade':[2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
                      'result':[67,132,89,123,135,123,111,134,78,123,78,89,133,134,112]})

df_10
df_pivot = df_10.pivot(index=['grade'], columns='age', values='result')
print(df_pivot)

# 宽格式转长格式
df_melt = df_pivot.melt(id_vars='grade', value_vars=['age', 'result'])


# pandas导入Csv文件
# CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）

# 读取csv数据
data_csv = pd.read_csv('示例csv数据.csv')
data_csv

data_csv.head()  # 读取前面的 n 行，如果不填参数 n ，默认返回 5 行

# 读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
data_csv.tail(10)

# 返回表格的一些基本信息：
data_csv.info()




print(data_csv.to_string())  # 返回 DataFrame 类型的数据


df_10

df_10.to_csv('dataframe_to_csv.csv')  # 文件夹自动创建一个csv文件



# Json数据格式
# JSON（JavaScript Object Notation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。

# 读取json数据
json_data = pd.read_json('json_data.json')
json_data

type(json_data)  # 存储为dataframe数据

print(json_data.to_string()) # 返回 DataFrame 类型的数据


# JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据


# 字典格式的 JSON                                                                                              
dict_1 = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame                                                                                          
dict_json = pd.DataFrame(dict_1)
print(dict_json)

# 从 URL 中读取 JSON 数据

URL = 'https://static.jyshare.com/download/sites.json'
URL_json = pd.read_json(URL)
print(URL_json)


# 内嵌的 JSON 数据
nest_jsondata = pd.read_json('nest_jsondata.json')
nest_jsondata

# 到 json_normalize() 方法将内嵌的数据完整的解析出来
# 使用 Python JSON 模块载入数据
import json

with open('nest_jsondata.json','r') as f:
    data_5 = json.loads(f.read())


# data = json.loads(f.read()) 使用 Python JSON 模块载入数据。

# json_normalize() 使用了参数 record_path 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students
# 展平数据
df_nested_list = pd.json_normalize(data_5, record_path =['students'])
print(df_nested_list)

# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：


# 使用 Python JSON 模块载入数据
with open('nest_jsondata.json','r') as f:
    data_6 = json.loads(f.read())

# 展平数据
df_nested_list_1 = pd.json_normalize(
    data_6,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list_1)


# 复杂的 JSON 数据，
mix_json = pd.read_json('mix_json.json')
mix_json
#  mix.json.json 文件转换为 DataFrame：

# 使用 Python JSON 模块载入数据
with open('mix_json.json','r') as f:
    data_7 = json.loads(f.read())
   
df_11 = pd.json_normalize(
    data_7,
    record_path =['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df_11)



# 数据清晰
# 导入数据、
test_data = pd.read_csv('test_data.csv')
test_data

# 数据含有4种空值，n/a,NA,-，na
# 删除包含空字段的行，可以使用 dropna() 方法
test_data.dropna()  # 不会修改源数据

# 修改源数据 DataFrame, 可以使用 inplace = True 参数
# test_data.dropna(inplace = True)

# 移除指定列有空值的行
test_data.dropna(subset = ['PID'])

# fillna() 方法来替换一些空字段
test_data.fillna(0)  # 用0替换缺失值

# 某一列数据的空缺值替换
test_data['PID'].fillna(0)


# average
average_value = test_data['PID'].mean()
average_value

# median
median_value = test_data['PID'].median()
median_value

# 众数
mod_value = test_data['ST_NUM'].mode()
mod_value



# 通过 isnull() 判断各个单元格是否为空。

print (test_data['PID'])
print (test_data['PID'].isnull())

# 指定空数据
missing_values = ["n/a", "na", "--"]
test_data_1 = pd.read_csv('test_data.csv', na_values = missing_values)

print (test_data_1['NUM_BEDROOMS'])
print (test_data_1['NUM_BEDROOMS'].isnull())



# 清洗格式错误数据
# 第三个日期格式错误
data_8 = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

data_8 = pd.DataFrame(data_8, index = ["day1", "day2", "day3"])
data_8
data_8['Date'] = pd.to_datetime(data_8['Date'], format='mixed')
data_8

# 清洗错误数据
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

data_9 = pd.DataFrame(person)
data_9
data_9.loc[2, 'age'] = 30 # 修改数据

# 设置条件语句
for x in data_9.index:
    if data_9.loc[x, "age"] > 45:
        data_9.loc[x, "age"] = 45
data_9


# 将错误数据删除
for x in data_9.index:
    if data_9.loc[x, "age"] > 40:
        data_9.drop(x, inplace = True)

data_9

# 清洗重复数据

person_copy = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}

data_10 = pd.DataFrame(person_copy)
data_10
data_10_uncopy = data_10.duplicated()
data_10_uncopy

# 使用drop_duplicates() 方法直接清除数据重复
data_10.drop_duplicates(inplace=True)
data_10

# pandas 常用函数
# 读取数据
pd.read_csv('test_data.csv') # 从csv中导入

pd.read_excel('a_excel.xlsx')  # 从excel中导入

pd.read_json('nest_jsondata.json') # 从json导入

# dfs = pd.read_html()
# pd.read_sql()

# 查看数据


# 显示前五行数据
df_10

# 显示前6行数据
df_10.head(6)

# 显示后五行数据
df_10.tail(5)

# 显示数据信息
df_10.info()

# 显示基本统计信息
df_10.describe()

# 显示数据的行数和列数
df_10.shape


#数据清洗
# 删除包含缺失值的行或列
df_10.dropna()

# 将缺失值替换为指定的值
df_10.fillna(0)

# 将指定值替换为新值
df_10.replace('old_value', 'new_value')

# 检查是否有重复的数据
df_10.duplicated()

# 删除重复的数据
df_10.drop_duplicates()


# 数据选择和切片

# 选择指定的列
df_10
df_10['grade']

# 通过标签选择数据
df_10.loc[2, 'age']

# 通过位置选择数据
df_10.iloc[10, 2]

# 通过标签或位置选择数据
df_10.ix[4, 'grade']

# 选择指定的列
df_10.filter(items=['grade', 'age'])

# 选择列名匹配正则表达式的列
df_10.filter(regex='regex')

# 随机选择 n 行数据
df_10.sample(n=5)

# 数据排序
# 按照指定列的值排序
df_10.sort_values('age')

# 按照多个列的值排序
df_10.sort_values(['result', 'grade'], ascending=[True, False])

# 按照索引排序
df_10.sort_index()


# 数据分组和聚合

df_7 = pd.DataFrame({'name':['da','bd','cs','ds','se'],
                     'age' :[12,13,12,11,12],
                     'grade':[2,5,2,3,3],
                     'result':[67,132,89,123,135]})
df_8 = pd.DataFrame({'name':['da','bd','cs','ds','se'],
                     'city':['da','bd','cs','ds','se'],
                     'sex' :[1,2,1,1,2]})
df_9 = pd.DataFrame({'name':['erf'],
                     'age' :[15],
                     'grade':[6],
                     'result':[32],
                     'city':['df'],
                     'sex' :[1]})
df_7
df_8
df_9


# 横向合并,merge有一列相同
pd_merge = pd.merge(df_7,df_8, on='name')
pd_merge



# 相关性分析

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
df
# 计算 Pearson 相关系数
correlation_matrix = df.corr()
print(correlation_matrix)

# 计算 Spearman 相关系数
spearman_correlation_matrix = df.corr(method='spearman')
print(spearman_correlation_matrix)

# 使用热图可视化 Pearson 相关系数
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


















