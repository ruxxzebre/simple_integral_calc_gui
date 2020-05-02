import PySimpleGUI as sg
import integral

sg.theme('DarkTeal2')   # Add a touch of color
# All the stuff inside your window.

menu_def = [['File', ['Exit',]],
                ['Help', ['About...', 'Help', 'Formulas used'],]]


layout = [  [sg.Menu(menu_def)],
            [sg.Text('SMALL INTEGRAL CALC')],
            [sg.Text('A :'), sg.InputText(do_not_clear=False, size=(10,1)), sg.Text('B :'), sg.InputText(do_not_clear=False, size=(10,1))],
            [sg.Text('Function'), sg.InputText(do_not_clear=False,  size=(32, 1))],
            [sg.Radio('Rectangle', 'METHOD', default=True), sg.Radio('Trapezoid', 'METHOD'), sg.Radio('Simpson', 'METHOD')],
            [sg.Checkbox('Detailed report')],
            [sg.Button('SOLVE'), sg.Text('Result :', border_width=5) , sg.Text('Empty', size=(50,1), key='_result_')] 
        ]

formulasUsedLayout = [
        [sg.Image('formula_1.png')],
        [sg.Image('formula_2.png')],
        [sg.Image('formula_3.png')]
]

# Create the Window
window = sg.Window('Integrals solver', layout, icon='integral.ico', size=(380,180))
formulasWindow = sg.Window('FORMULAS USED', formulasUsedLayout, icon='integral.ico', size=(500,320))
# Event Loop to process "events" and get the "values" of the inputs

if __name__ == '__main__':
    #sg.theme_previewer()
    while True:
        event, values = window.read()

        if event in (None, 'Exit'):   # if user closes window or clicks cancel
            break

        if event == 'About...':
            sg.Popup('Integral calculation app by Pavlo Chaikovskyi 125B')  
        elif event == 'Formulas used':
            formulasWindow.read()
        elif event == 'Help':
            sg.Popup('HELPER', 'Into "A" field enter upper limit\nInto "B" field enter lower limit\nAnd into expression - enter your function\nlike - x**2\nIf you want detailed result\nwith memory usag and time - \nclick certain checkbox')

        
        if '' not in values.values() and event == 'SOLVE':
            #print(event)
            #print(values)
            print(values)
            if values[3] == True:
                method = 'Rectangle method'
            elif values[4] == True:
                method = 'Trapezoid method'
            elif values[5] == True:
                method = 'Simpson method'
            result = integral.processArguments([values[1], values[2], values[3]], method)
            print(values)
            if values[7] == True:
                sg.Popup(f'RESULT: {result[0]}', result[1], result[2])
            else:
                window.Element('_result_').Update(str(result[0]))
        elif event == 'SOLVE':
            sg.Popup('Opps!', 'One of the fields is empty.')


        

    window.close()
    