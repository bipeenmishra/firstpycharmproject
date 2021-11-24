import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
new1 = df2['customer_name'].tolist()
pro = df2['product_line'].tolist()
Volume = df2['volume_in_kg'].tolist()
Gross = df2['gross_sales'].tolist()
margin = df2['gm'].tolist()


def my_function(dup):
    return list(dict.fromkeys(dup))


mylist = my_function(new1)

print('Unique Customer', mylist)


def my_fun(myfun):
    return list(dict.fromkeys(myfun))


mylis = my_fun(pro)

print('Unique product', mylis)


def my_function(Vol):
    return sum(Vol)


print('Sum of Volume', my_function(Volume))


def my_function(Vol):
    return np.mean(Vol)


print('Mean of Volume', my_function(Volume))


def my_function(Vol):
    return np.median(Vol)


print('Median of Volume', my_function(Volume))


def my_function(Vol):
    return np.min(Vol)


print('Min of Volume', my_function(Volume))


def my_function(Vol):
    return np.max(Vol)


print('Max of Volume', my_function(Volume))


def my_function(Vol):
    return np.std(Vol)


print('Std of Volume', my_function(Volume))


def my_function(Vol):
    return np.var(Vol)


print('Var of Volume', my_function(Volume))


def my_function(Gs):
    return sum(Gs)


print('Sum of Sales', my_function(Gross))


def my_function(Gs):
    return np.mean(Gs)


print('Mean of Sales', my_function(Gross))


def my_function(Gs):
    return np.median(Gs)


print('Median of Sales', my_function(Gross))


def my_function(Gs):
    return np.min(Gs)


print('Min of Sales', my_function(Gross))


def my_function(Gs):
    return np.max(Gs)


print('Max of Sales', my_function(Gross))


def my_function(Gs):
    return np.std(Gs)


print('Std of Sales', my_function(Gross))


def my_function(Gs):
    return np.var(Gs)


print('Var of Sales', my_function(Gross))


def my_function(Gm):
    return sum(Gm)


print('Sum of Margin', my_function(Gross))


def my_function(Gm):
    return np.mean(Gm)


print('Mean of Margin', my_function(margin))


def my_function(Gm):
    return np.median(Gm)


print('Median of Margin', my_function(margin))


def my_function(Gm):
    return np.min(Gm)


print('Min of Margin', my_function(margin))


def my_function(Gm):
    return np.max(Gm)


print('Max of Margin', my_function(margin))


def my_function(Gm):
    return np.std(Gm)


print('Std of Margin', my_function(margin))


def my_function(Gm):
    return np.var(Gm)


print('Var of Margin', my_function(margin))

Volume = df2["gross_sales"]
Sales = df2["volume_in_kg"]
x = []
y = []


def Scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Volume')
    plt.ylabel('Sales')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    x = list(Volume)
    y = list(Sales)
    Scatter_plot(x, y)


def line_plot(x, y):
    plt.plot(x, y)
    plt.xlabel('Volume')
    plt.ylabel('Sales')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    x = list(Volume)
    y = list(Sales)
    line_plot(x, y)

chunk = df2[['churn_proba']].sum()
cf = df2[['churn_proba']].count()
avg = chunk / cf
print('Amount of average chunk is', avg)

df3 = pd.read_csv('C:\\Users\\mishr\\Downloads\\Tweleve.csv', usecols=['customer_name']).drop_duplicates(keep='first')
cus_chunk = df3[['customer_name']].count()
df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', usecols=['customer_name']).drop_duplicates(keep='first')
cust = df2[['customer_name']].count()
average = cus_chunk / cust * 100
print('Customer churned', round(average))

