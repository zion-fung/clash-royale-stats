import xlsxwriter as xw
import royaleapi as rapi
biochem_warfare = "Y900LQ8L"
savage_bros = "R2OV8L"

if __name__ == "__main__":
	workbook = xw.Workbook("tester.xlsx")
	worksheet = workbook.add_worksheet()
	clan = rapi.get_clan(savage_bros)
	row = 0
	worksheet.write(row, 0, "Name")
	row += 1
	for mem in clan["members"]:
		worksheet.write(row, 0, mem["name"])
		worksheet.write(row, 1, mem["expLevel"])
		row += 1
	workbook.close()