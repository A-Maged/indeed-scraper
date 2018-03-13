import sys
import xlwt


def print_excel( job_details):

  # initailize a spreadsheet
  book = xlwt.Workbook(encoding="utf-8")
  sheet  = book.add_sheet("Sheet 1" )

  # write columns headers
  sheet_headers =[ 'job title', 'snippet', 'date', 'company', 'city', 'state', 'formatted Location Full', 'sponsored', 'url', 'job key' ]

  for header_indx, header in enumerate(sheet_headers):
    sheet.write(0 , header_indx,  header  , xlwt.easyxf("align: horiz center "  ))

  for row, jobb in enumerate(job_details):
      for col, item in enumerate( jobb):
          try:
                # cell width
                item_length = len(item)
                if item_length < 50:
                  sheet.col(col).width = ( item_length + 13) * 250
                elif item_length < 15:
                  sheet.col(col).width = 25 * 250
                else:
                  sheet.col(col).width = 30 * 250
          except:
                  sheet.col(col).width = 15* 250
                  pass

          # write item
          row = row +1
          sheet.write(row , col,  item   , xlwt.easyxf("align: horiz left"  ))
          row= row -1

  sheet.col(2).width = 30 * 250
  sheet.col(3).width = 22 * 250
  sheet.col(4).width = 18 * 250
  sheet.col(5).width = 6 * 250
  sheet.col(7).width = 5 * 250

  book.save("aaa.xls")
  sys.exit(0)
