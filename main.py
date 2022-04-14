#Briana DeAndrade

import openpyxl
import numbers
import openpyxl.utils
import plotly.graph_objects
from state_abbrev import us_state_to_abbrev

def main():
    pop_worksheet = open_worksheet("countyPopChange2020-2021.xlsx")
    show_pop_change = should_display_pop_change()
#This is where I need some help calling variables depending on if t/f

    if show_pop_change == True:
         show_pop_change_map(pop_worksheet)
    else:
         show_percent_change_map(pop_worksheet)

def open_worksheet(file):
    pop_excel = openpyxl.load_workbook(file)
    data_sheet = pop_excel.active
    return data_sheet

def should_display_pop_change():
    show_pop_change = input ("Should the program display a map of total population changes?")
    if show_pop_change == "yes":
        return True
    else:
        return False

def show_pop_change_map(data_sheet):
    list_of_state_abbrev = []
    list_of_pop_changes = []
    for row in data_sheet.rows:
        state_total = row[4]
        pop_change = row[11]
        state_abbrev = row[5]


def show_percent_change_map():
    pass

main()