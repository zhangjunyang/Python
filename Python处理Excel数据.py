data = pd.read_csv('text_emotion.csv')
# 删除列author
data = data.drop('author', axis=1)
#删除行rows with anger emotion labels
data = data.drop(data[data.sentiment == 'anger'].index)
# 显示数据的行与列数
data.shape
# 显示列名
data.columns
# 查看数据格式dtpyes
data.dtypes
data.head(10)
data.tail(10)
# 所有缺失值显示为True
# data.isnull()
# 删除空值 
data.dropna(how='any')
# 空值用0填充
data.fillna(value=0)
 # 利用sentiment的均值对缺失值进行填充
data['sentiment'].fillna(data['sentiment'].mean())


