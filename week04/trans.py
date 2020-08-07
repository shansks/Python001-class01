import pandas as pd
from pandas import DataFrame

table1=DataFrame([{"id":10,"name":'lxh',"age":20,"cp":'lm'},{"id":1,"name":'xiao',"age":40,"cp":'ly'},{"id":2,"name":'hua',"age":4,"cp":'yry'},{"id":3,"name":'be',"age":70,"cp":'old'}],index=['a','b','c','d'])
table2=DataFrame([{"sex":0},{"sex":1},{"sex":2}],index=['a','b','e'])

# 1. SELECT * FROM data;
data = pd.read_csv('data.csv')
# print(data)

# 2. SELECT * FROM data LIMIT 10;
# head10 = data.head(10)
# print(head10)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
# id_index = data[['id']]
# print(id_index)

# 4. SELECT COUNT(id) FROM data;
# id_count = data[['id']]
# print(id_count.count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
# query = data[(data['id']>1000)&(data['age']<30)]
# print(query)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# data.drop_duplicates(subset=['order_id'],keep='first')
# for a,b in data.groupby('id'):
#     print(a)
#     print(b)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# pd.merge(table1,table2,on='id',how='inner')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
# table1.join(table2)

# 9. DELETE FROM table1 WHERE id=10;
# nf = table1.drop(table1[table1.id==10].index)
# print(nf)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
# nf = table1.drop(['name'],axis=1)
# print(nf)