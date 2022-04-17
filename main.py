#Briana DeAndrade
#Running it successfully is currently left undone/incomplete
#In order to run the program correctly, the user will need to respond "yes" into the first prompted question: ""Should the program display a map of total population changes?"

#Here I imported openpyxl for the excel work, numbers for the math that we will do later in the code, plotly.graph for the graphs and state_abbrev to work with the states and abbreviations later on
import openpyxl
import numbers
import openpyxl.utils
import plotly.graph_objects
from state_abbrev import us_state_to_abbrev

#Here is my main function. This is where I called the worksheet and stored it in a variable.
#I also called the should _display_pop_change fxn and stored it in the variable.
#Lastly, I established an if statment so that if the user returns "yes" (True) then a certain fxn/map would be presented and if "else", another fxn/map would
def main():
    pop_worksheet = open_worksheet("countyPopChange2020-2021.xlsx")
    show_pop_change = should_display_pop_change()
    if show_pop_change == True:
        show_pop_change_map(pop_worksheet)
    else:
        show_percent_change_map(pop_worksheet)

#In this open_worksheet fxn, the excel file was opened, the contencts were read and the worksheet was returned in the fxn
def open_worksheet(file):
    pop_excel = openpyxl.load_workbook(file)
    data_sheet = pop_excel.active
    return data_sheet

#This is the fxn where the user is prompted the initial question and if they respond "yes", the fxn returns true and if anything else, returns false
def should_display_pop_change():
    show_pop_change = input ("Should the program display a map of total population changes?")
    if show_pop_change == "yes":
        return True
    else:
        return False

#In the show_pop_change_map fxn, we establish the state names/abbrev's and also a for loop
#This goes through the database and displays 2021 populations and state abbrev's on a map using plotly
def show_pop_change_map(data_sheet):
    list_of_state_abbrev = []
    list_of_pop_changes = []
    for row in data_sheet.rows:
        pop_change_cell = row[11]
        name_cell = row[5]
        state_name = name_cell.value
        state_abbrev = us_state_to_abbrev[state_name]
        list_of_state_abbrev.append(state_abbrev)
        pop_change = pop_change_cell.value
        list_of_pop_changes.append(pop_change)

    map_to_show = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Choropleth(
            locations=list_of_state_abbrev,
            z=list_of_pop_changes,
            locationmode="USA-states",
            colorscale='Picnic',
            colorbar_title='population amount'
        )
    )
    map_to_show.update_layout(
        title_text="Population Change 2020 to 2021",
        geo_scope="usa"
    )
    map_to_show.show()

#In the show_poercent_change_map fxn, we establish the state names/abbrev's again and also a for loop
#This goes through the database and displays 2021 populations PERCENT CHANGES on a map using plotly
def show_percent_change_map():
    list_of_state_abbrev = []
    list_of_pop_changes = []
    for row in data_sheet.rows:
        state_cell = row[5]
        population_change = row[11]
        pop_est = row[9]
        percent_population_est = pop_est.value
        pop_change = population_change.value
        population_change_percent = pop_change / percent_population_est
    state_abbrev = us_state_to_abbrev[state_cell]
    list_of_state_abbrev.append(state_abbrev)
    list_of_pop_changes.append(population_change_percent)
    map_to_show = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Choropleth(
            locations=list_of_state_abbrev,
            z=list_of_pop_changes,
            locationmode="USA-states",
            colorscale='Picnic',
            colorbar_title="population amount",
        )
    )
    map_to_show.update_layout(
        title_text="Percent Change Map",
        geo_scope="usa"
    )
    map_to_show.show()
main()