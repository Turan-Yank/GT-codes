import math as mt
import numpy as np
import xlsxwriter as xl

workbook = xl.Workbook('Design_Points.xlsx')
worksheet = workbook.add_worksheet()

r = 0
c = 0
worksheet.write(r, c, "C")
worksheet.write(r, c+1, "A")
worksheet.write(r, c+2, "D")
worksheet.write(r, c+3, "B")
worksheet.write(r, c+4, "alfa")
r+=1

for A in np.arange(1.1, 2.1, 0.2):
    for B in np.arange(1.1, 2.1, 0.2):
        for C in np.arange(0.1, 2, 0.2):
            for D in np.arange(0.1, 1.1, 0.2):
                alfa=(180.*(mt.atan((A-D)/(B-C))))/mt.pi
                h=mt.sqrt(mt.pow((A-D),2.)+mt.pow((B-C),2.))
                if ((alfa > 0 and alfa < 86.98) and (B != C and h <= 1.9026)):
                    t="DP "+ str(r) + "," + str(C) +"," + str(A) + "," + str(D) + "," + str(B)
                    worksheet.write(r, c, t)
                    r+=1

workbook.close()
