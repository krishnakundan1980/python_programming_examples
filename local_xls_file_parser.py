### Python programing example for:
### 1. Parsing a xlsx file using xlrd python package
### 2. Creating xlsx file and populating with data
### 3. Loading existing xlsx file and updating data fields

import sys
import xlrd # Read only
import xlsxwriter#Just for creating xlsx file not for updating existing xlsx fle
import re# for regular expression usage
import openpyxl#updating existing xlsx file

tupLookupVal1 = ('physics', 'chemistry', 'math', 'english');
tupLookupVal2 = (1234, 3456, 4567, 7890);

dicOfClassificationData = {}#Show how to use global variable  

def load_and_parse_xlsx_file(file_name):
    global dicOfClassificationData
    workbook = xlrd.open_workbook(file_name)
    for sheet_name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(sheet_name)
        #get row and column index
        dicOfEquipmentData = {}
        for col in range(sheet.ncols):
            if col > 2:
                equipmentData = []
                for row in range(sheet.nrows):
                    if row > 1:
                        equipmentData.append((sheet.cell_value(row,1), sheet.cell_value(row ,col)))
                dicOfEquipmentData[sheet.cell_value(1,col)] = equipmentData
        dicOfClassificationData[sheet_name] = dicOfEquipmentData

    
def populate_data_in_output_file():
   global dicOfClassificationData
   workbook2 = xlsxwriter.Workbook('output.xlsx')
   worksheet = workbook2.add_worksheet('output')
   equip_attr_counter =1;
   for sheet in dicOfClassificationData.keys():
       for equipment in dicOfClassificationData[sheet].keys():
           for item in dicOfClassificationData[sheet][equipment]:
               worksheet.write('A{0}'.format(equip_attr_counter), equipment)
               worksheet.write('B{0}'.format(equip_attr_counter), item[0])
               worksheet.write('C{0}'.format(equip_attr_counter), item[1])
               equip_attr_counter = equip_attr_counter + 1
   workbook2.close()

def Validate_Attributes_DataField():
    global dicOfClassificationData
    #try:
    xfile = openpyxl.load_workbook('output.xlsx')
    sheet = xfile.active#get_sheet_by_name('output')
    attrCol = 'B'
    attrValCol = 'C'
    row = 1
    while (row <= 86):
        attrName = sheet[attrCol + str(row)].value
        attrVal = sheet[attrValCol + str(row)].value
        if attrName == 'Attr1':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
            sheet['G' + str(row)] = ApplyNARule(attrName, attrVal)
            sheet['H' + str(row)] = ApplyNoSpaceWithinValue(attrName, attrVal)
            sheet['I' + str(row)] = ApplyDigitOnly(attrName, attrVal)
        elif attrName == 'Attr2':
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
            sheet['G' + str(row)] = ApplyNARule(attrName, attrVal)
            sheet['H' + str(row)] = ApplyNoSpaceWithinValue(attrName, attrVal)
        elif attrName == 'Attr3':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr4':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr5':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr6':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr7':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr8':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        elif attrName == 'Attr9':
            sheet['D' + str(row)] = ApplyNonEmptyRule(attrName, attrVal)
            sheet['E' + str(row)] = ApplyLookupTable1(attrName, attrVal)
            sheet['F' + str(row)] = ApplyLookupTable2(attrName, attrVal)
        row = row + 1
    #except:
     #   print("Unexpected error:", sys.exc_info())
        
    xfile.save('output.xlsx')


def ApplyNonEmptyRule(attrName, attrVal):
    if attrVal == "":
        return 1
    else:
        return 0

def ApplyLookupTable1(attrName, attrVal):
    if attrVal not in tupLookupVal1:
        return 1
    else:
        return 0

def ApplyLookupTable2(attrName, attrVal):
    if attrVal not in tupLookupVal2:
        return 1
    else:
        return 0

def ApplyNARule(attrName, attrVal):
    if attrVal == "NA":
        return 1
    else:
        return 0

def ApplyNoSpaceWithinValue(attrName, attrVal):
    if re.search(r"\s", '%s' % (attrVal)):
        return 0
    else:
        return 1

def ApplyDigitOnly(attrName, attrVal):
    if ('%s' % (attrVal)).isdigit():
        return 0
    else:
        return 1

def ApplyAlphabetOnly(attrName, attrVal):
    if ('%s' % (attrVal)).isalpha():
        return 0
    else:
        return 1
    

def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)
    
    load_and_parse_xlsx_file(sys.argv[1])
    print(sys.argv[1])
    populate_data_in_output_file()
    Validate_Attributes_DataField()

if __name__ == '__main__':
  main()