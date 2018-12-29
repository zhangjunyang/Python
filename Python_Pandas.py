# 索引
print(df.index)

# 列标签
print(df.columns)

# 数值
print(df.values)

# 统计
print(df.describe())

# 转置
print(df.T)

# 按轴排序，逐列递减
print(df.sort_index(axis=1, ascending=False))

# 按值排序，'B'列逐行递增
print(df.sort_values(by='B'))

# 选中一整行
print(df.loc[dates[0]])

# 按标签选中复数列（所有行，输出只显示前5行）
print(df.loc[:,['A','B']])

# 行/列同时划分（包括起止点）
print(df.loc['20130102':'20130104',['A','B']])

# 返回一个元素（两个方法等效）
print(df.loc[dates[0],'A'])
print(df.at[dates[0],'A'])

# 位置索引为3的行（从0开始，所以其实是第4行）
print(df.iloc[3])

# 按位置索引分割DataFrame
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

# 直接定位一个特定元素
df.iloc[1,1]
df.iat[1,1]

# 用一列的值来选择数据
print(df.A > 0)

# 使用.isin()函数过滤数据
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

# 提取df2中'E'值属于['two', 'four']的行
print(df2[df2['E'].isin(['two','four'])])

# 剔除df1中含NaN的行（只要任一一列为NaN就算）
df1.dropna(how='any')

# 用5填充df1里的缺失值
df1.fillna(value=5)

# 判断df1中的值是否为缺失数据，返回True/False
pd.isnull(df1)

# 将索引为3的行增补到整个DataFrame最后
s = df.iloc[3]
print(df.append(s, ignore_index=True))

# 对'A'列进行合并并应用.sum()函数
print(df.groupby('A').sum())

# 对'A', 'B'两列分别合并形成层级结构，再应用.sum()函数
print(df.groupby(['A','B']).sum())

# 输出至.csv文件
df.to_csv('haha.csv')

# 从.csv文件中读取数据
pd.read_csv('haha.csv')

# 输出至.xlsx文件
df.to_excel('haha.xlsx', sheet_name='Sheet1')

# 从.xlsx文件中读取数据
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
('haha.csv')

