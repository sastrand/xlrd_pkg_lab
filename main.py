# [add an import statment here]
import xlrd

def open_fish_file():
    """
    Opens `pdx_fish.xls` and returns contents as column-major list of
    lists.
    """
    pdx_fish_file = "./pdx_fish_test.xls"
    wb = xlrd.open_workbook(pdx_fish_file)

    # takes the first worksheet in the workbook
    pdx_fish = wb.sheet_by_index(0)

    # sets cursor to row 0, column 0
    pdx_fish.cell_value(0, 0)

    # iterates through xlrd worksheet and copies values to list of lists
    worksheet = list()
    for col in range(pdx_fish.ncols):
        worksheet.append(list())
        for row in range(pdx_fish.nrows):
            worksheet[col].append(pdx_fish.cell_value(row, col))

    return worksheet


def print_worksheet(worksheet):
    """
    Takes a worksheet in the form of a column-major list of lists
    and prints it to std out.
    """
    for col in range(len(worksheet)):
        for row in range(len(worksheet[0])):
            print(worksheet[col][row])
        print("\n")


if __name__ == "__main__":
    ws = open_fish_file()
    print_worksheet(ws)
