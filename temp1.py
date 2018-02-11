import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import xlsxwriter
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import helper

helper.clearscreen()
boston1=datasets.load_boston()

boston1df=pd.DataFrame(boston1.data)
boston1df.columns=boston1.feature_names

#X & y data prep
print("boston1 price target = ",boston1.target[:5])
boston1df['PRICE']=boston1.target #Add PRICE as boston1df column
X=boston1df.drop('PRICE',axis=1) #drop the PRICE column since we want X to be predictors only

#Perform Linear Regression
lm=LinearRegression()
lm.fit(X,boston1df.PRICE) #find coeff that allow hitting boston1df.PRICE given X 
#print("Predictors = ",X,"\n")    
estcoeff=pd.DataFrame([[X.columns,lm.coef_]],columns=['Variables','Estimated Coefficients'])
print("Variables & their Estimated Coefficients are ",estcoeff,"\n")
estcoeffarr=estcoeff.as_matrix()
print(estcoeffarr,"\n")

#Perform Prediction
print("Estimated PRICE = ",lm.predict(X)[0:5],"\n")
#plt.scatter(boston1arr[0][:],boston1arr[1][:])
plt.scatter(boston1df.PRICE,lm.predict(X))
plt.xlabel("Actual Price, $Y_i$ (USD)") #$Y_i$ = Y subscript i
plt.ylabel("Predicted Price ${hat}Y_i$ (USD)")
plt.title("Predicted VS Actual Prices, ${hat}Y_i$ VS  $Y_i$")
plt.savefig('Predicted_Actual_Prices.png')

MSE_X_All=np.mean((boston1df.PRICE-lm.predict(X))**2)
print("Mean Squared Error when using all predictors in X = ",MSE_X_All,"\n")

lm.fit(X[["CRIM"]],boston1df.PRICE)
MSE_X_CRIM=np.mean((boston1df.PRICE-lm.predict(X[["CRIM"]]))**2)
print("Mean Squared Error when using only CRIM as predictor in X = ",MSE_X_CRIM,"\n")

#Plot in Excel
boston1arr=np.array(boston1.data)
print("boston1 data dimensions = ",boston1arr.shape,"\n")
arrshape=boston1arr.shape
print(arrshape)
nrows=arrshape[0]
ncols=arrshape[1]

#helper.writetoCSV('boston_data4.csv',boston1arr,1,2,3)
helper.writetoCSV2('boston_data4.csv',boston1arr,2,4,6)
#helper.writetoCSVNested('boston_data5.csv',boston1arr)
helper.writetoCSV3('boston_data5.csv',boston1arr,2,4,6)

with open('boston_data2.csv','w') as f:
    for row in range(0,nrows):
        if row==0:
            f.write("")
        else:
            f.write("\n")
        for col in range(0,ncols):
            f.write("%s " % boston1arr[row,col])

wb1=xlsxwriter.Workbook('boston_data3.xlsx')
wb1ws1=wb1.add_worksheet()
boston1newfeatures=np.append(boston1.feature_names,"PRICE")
for row in range(0,nrows):
    for col in range(0,ncols):
        if row==0:
            wb1ws1.write(row,col,"%s "% boston1newfeatures[col])
        else:
            wb1ws1.write(row,col,"%s\n" % boston1arr[row,col])  
wb1.close()

wb1ws2=wb1.add_worksheet()
[wb1ws2.write(row,col,"%s\n" % boston1arr[row,col]) for row in range(0,nrows) for col in range(0,ncols) ]
wb1.close()


#plt.scatter(boston1arr[0][1],lm.predict(X[0][1]))
#estcoeffarrshape=estcoeffarr.shape()
#ecnrow=estcoeffarrshape[0]
#ecncol=estcoeffarrshape[1]
#
#wb1ws3=wb1.add_worksheet()
#[wb1ws3.write(row,col,"%s\n" % estcoeffarr[ecnrow,ecncol]) for row in range(0,ecnrow) for col in range(0,ecncol) ]
#
#plt.scatter(boston1df['LSTAT'],lm.predict(X)) #compare actual & predicted LSTAT


#wb1.close()

#with xlsxwriter.Workbook('boston_data3.xlsx') as wb1:
#    with wb1.add_worksheet() as wb1ws1:
#        for row in range(0,nrows):
#            for col in range(0,ncols):
#                wb1ws1.write(row,col,"%s\n" % boston1arr[row,col])

#wb1=xlsxwriter.Workbook('boston_data3.xlsx')
#wb1ws1=wb1.add_worksheet()
#wb1ws1.writelines(["%s\n" % elm in boston1arr])
#wb1.close()
#f=open('boston_data.csv','w')
#f.writelines(["%s\n"% el for el in boston1arr] )
#f.write("\n")
#f.close()