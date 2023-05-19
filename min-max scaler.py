import pandas as pd
class MinMaxNorm:
  def scale(self,d):
    for i in d.columns:
      min=d[i].min()
      max=d[i].max()
      d[i]=(d[i]-min)/(max-min)
    return d
data=pd.DataFrame([[60000,32],[50000,25],[70000,40],[70000,32]],columns=['Salary','Age'])
print("Original Data")
print(data)
s=MinMaxNorm()
print("\nScaled Data")
df=s.scale(data)
print(df)
