import csv

'''
this function toCSVFile is used to 
	convert param dataList to one csv file which contain value and result(pass/fail); 
	paramType means: which param you want to   
'''
def toCSVFile(dataList, paramType = "GantryAngle"):
	csvFile = open("E:/Unimelb IT/semester3-2/software project/Sprint1/test.csv", 'w', newline='')
	try:
		writer=csv.writer(csvFile)
		writer.writerow((paramType+" #",'value','result'))
		for i in range(len(dataList)):
			flag = dataList[i]>50 and dataList[i]<120
			writer.writerow((i, dataList[i], flag))
	finally:
		csvFile.close()

#  sample test, if
dataList = [100,110,80,200]
toCSVFile(dataList)