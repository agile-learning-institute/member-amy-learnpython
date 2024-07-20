import pandas as pd


def hello():
    return("Hello World")

def goodbye(name):
    return("goodbye "+name)
    
def panda():
    color = ['blue','green','red','yellow']
    fruit = ['blueberry','apple','cherry','banana']
    df=pd.DataFrame(columns=['color', 'fruit'])
    df['COLOR'],df['FRUIT']=color,fruit
    return(df)