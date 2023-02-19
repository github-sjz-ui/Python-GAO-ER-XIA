import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12.8,7.2),dpi=800)
df=pd.read_excel("高二期末成绩20030212.xlsx")
'''
# 排名
ranking_yuwen=pd.DataFrame(df.语名).set_index(df.姓名)
ranking_shuxue=pd.DataFrame(df.数名).set_index(df.姓名)
ranking_yingyu=pd.DataFrame(df.英名).set_index(df.姓名)
ranking_wuli=pd.DataFrame(df.物名).set_index(df.姓名)
ranking_huaxue=pd.DataFrame(df.化名).set_index(df.姓名)
ranking_shengwu=pd.DataFrame(df.生名).set_index(df.姓名)
ranking_zhengzhi=pd.DataFrame(df.政名).set_index(df.姓名)
ranking_lishi=pd.DataFrame(df.历名).set_index(df.姓名)
ranking_dili=pd.DataFrame(df.地名).set_index(df.姓名)
ranking_jishu=pd.DataFrame(df.技名).set_index(df.姓名)
# 人数
number_yuwen=df.语文.count()-(df['语文']==0).sum()
number_shuxue=df.数学.count()-(df['数学']==0).sum()
number_yingyu=df.英语.count()-(df['英语']==0).sum()
number_wuli=df.物理.count()-(df['物理']==0).sum()
number_huaxue=df.化学.count()-(df['化学']==0).sum()
number_shengwu=df.生物.count()-(df['生物']==0).sum()
number_zhengzhi=df.政治.count()-(df['政治']==0).sum()
number_lishi=df.历史.count()-(df['历史']==0).sum()
number_dili=df.地理.count()-(df['地理']==0).sum()
number_jishu=df.技术.count()-(df['技术']==0).sum()
'''
# 输入
name=input('请输入人名：')
# 判断选科
all_xuanke=['语文','数学','英语','物理','化学','生物','政治',\
           '历史','地理','技术']
score=[]
name=df[df.姓名==name]
xk=[]
list=['语名','数名','英名','物名','化名','生名',\
               '政名','历名','地名','技名']
for i in all_xuanke:
    if not name[i].empty:
        xk.append(i)
        number=df[i].count()-(df[i]==0).sum()
        score.append(1-int(name[list[all_xuanke.index(i)]])/number)

