读取数据
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series, DataFrame

import xlrd
df = xlrd.open_workbook('x.xlsx')

import  pandas as pd
df = pd.read_excel('x.xlsx')
df = pd.read_csv('x.csv')

显示数据
    显示数据的行与列数
    df.shape

    查看数据格式dtpyes
    df.dtypes

    显示列名
    df.columns

    添加默认的列名
    df = pd.read_excel('x.xlsx', header = None) 
    #显示前数据前5行
    df.head(5)

    显示数据后5行
    df.tail(5)

    显示数据唯一值
    df['经纪人级别'].unique()

    跳过文件的第i行不读取
    # 没有读取经纪人编号为20124403的行
    df = pd.read_excel('x.xlsx',skiprows=[2] ) 
    df.head()

    对缺失值进行识别
    # 所有缺失值显示为True
    # df.isnull()
    pd.insull(df)

数据清洗
    处理空值
    df.dropna(how='any')
    # 空值用0填充
    df.fillna(value=0)
     # 利用经纪人响应时长的均值对缺失值进行填充
    df['经纪人响应时长'].fillna(df['经纪人响应时长'].mean())

    更改数据格式
    df['大区'].astype('float64')

    更改列名称
    df.rename(columns={'IM渠道': '渠道'})

    删除重复值
    #使用默认第一次出现的被保留，后面出现的被删除
    df['门店'].drop_duplicates()
    df['门店'].drop_duplicates(keep = 'last')

    对列表内的值进行替换
    df['客户UCID'].replace('10531975', '110')

数据预处理
    对数据进行排序
    df.sort_values(by=['客户当天发送消息数'])

    数据分组
    #如果price列的值>3000，group列显示high，否则显示low
    df['group'] = np.where(df['客户当天发送消息数'] > 5,'high','low')
    df

    # 符合经纪人级别为A1且经纪人响应时长>24的在sign列显示为1
    df.loc[(df['经纪人级别'] == 'A1') & (df['经纪人响应时长']>= 24.0), 'sign']=1
    df

    数据分列
    pd.DataFrame((x.split('网') for x in df['客户注册渠道']),index=df.index,columns=['客户注册渠道','size'])

数据提取
    # 按标签提取0-3行的数据：loc函数
    df.loc[0:3]

    # 按日期进行提取
    # 重新设置索引
    df.reset_index()
    #设置日期为索引
    df=df.set_index('日期')
    #提取2016年11月2号的数据
    df[‘2016-11-2’ : '2016-11-02']

    按位置提取：iloc函数
    # 按区域提取
    df.iloc[:4, :5]
    # 按位置提取
    #[0, 2, 5] 代表指定的行，[ 4, 5 ] 代表指定的列
    df.iloc[[0,2,5],[4,5]]
    按标签和位置提取
    # 行按日期排列，列按位置设置
    df.ix['2016-11-03':'2016-11-03',4:6]

    按条件提取:loc与isin函数
    # 判断经纪人级别是否为A3
    df['经纪人级别'].isin(['A3'])
    #先判断经纪人级别列里是否包含A3和M4，然后将复合条件的数据提取出来。
    df.loc[df['经纪人级别'].isin(['A3','M4'])]

    从合并的数值中提取出指定的数值
    # 提取链家网三个字
    data = df['客户注册渠道']
    pd.DataFrame(data.str[:3])

数据筛选
    按条件筛选
    #级别为M4，发送消息数大于110
    df.loc[(df['经纪人当天发送消息数'] > 110) & (df['经纪人级别'] == 'M4'), 
            ['经纪人响应时长','是否5分钟内响应','经纪人系统号']]

    #发送消息数大于400或响应时长大于60000
    df.loc[(df['经纪人当天发送消息数'] > 400) | (df['经纪人响应时长'] > 60000.0), 
        ['经纪人响应时长','经纪人系统号']].sort(['经纪人响应时长'])

    #筛选完可直接求和
    df.loc[(df['经纪人当天发送消息数'] > 400) | (df['经纪人响应时长'] > 60000.0),
            ['经纪人响应时长','经纪人系统号']].sort(['经纪人响应时长']).经纪人响应时长.sum()

    df.loc[(df['经纪人当天发送消息数']!= 200) & (df['经纪人级别'] == 'A4'),
       ['经纪人响应时长','经纪人系统号']].sort(['经纪人响应时长'])

    # count() 算总数
    df.loc[(df['经纪人当天发送消息数']!= 200) & (df['经纪人级别'] == 'A4'),
            ['经纪人响应时长','经纪人系统号']].sort(['经纪人响应时长']).经纪人系统号.count()

    # 使用query函数
    df.query('经纪人级别 == ["A4", "M4"]')

数据汇总
    分类汇总:groupby
    # 对所有列进行分类汇总
    df.groupby('经纪人级别').count()

    # 对特定列进行汇总
    df.groupby('经纪人级别')['经纪人响应时长'].count()

    # 增加分类条件
    df.groupby(['经纪人级别','经纪人是否回复'])['经纪人响应时长'].count()

    # 进行分组并进行算数运算
    # 对经纪人响应时长进行分类汇总，并计算均值
    df.groupby('经纪人级别')['经纪人响应时长'].agg([ np.mean])

    数据透视
    pd.pivot_table(df,index=["经纪人当天发送消息数"],values=["经纪人响应时长"],
          columns=["经纪人级别"],aggfunc[len,np.sum],fill_value=0,margins=True)

数据统计
    数据采样
    # 简单随机抽取sample
    df.sample(n=3)

    # 设置采样权重
    weights = [0, 0, 0.5, 0.5]
    df.sample(n=4, weights=weights)

    # 确定采样后是否放回
    # 采样后放回，True
    df.sample(n=6, replace=True)

    描述统计:describe函数
    # 自动生成数据的数量，均值，标准差等数据
    #round（2）,显示小数点后面2位数，T转置
    df.describe().round(2).T

    # 标准差std()
    df['经纪人响应时长'].std()

    协方差:cov
    #计算两个字段之间的协方差
    df['经纪人当天发送消息数'].cov(df['客户当天发送消息数'])

    相关性分析:corr
    # 相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关
    df['客户当天发送消息数'].corr(df['经纪人当天发送消息数'])

