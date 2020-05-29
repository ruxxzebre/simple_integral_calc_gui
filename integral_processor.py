import PySimpleGUI as sg
#import PySimpleGUI import Windows
import integral

class GUI:
    def __init__(self, theme='DarkTeal2'):
        sg.theme(theme)
        window_menu = [['File', ['Exit',]],['Help', ['About...', 'Help', 'Formulas used'],]]
        self.layout = [  [sg.Menu(window_menu)],
                [sg.Text('SMALL INTEGRAL CALC')],
                [sg.Text('A :'), sg.InputText(do_not_clear=False, size=(10,1)), sg.Text('B :'), sg.InputText(do_not_clear=False, size=(10,1))],
                [sg.Text('Function'), sg.InputText(do_not_clear=False,  size=(32, 1))],
                [sg.Radio('Rectangle', 'METHOD', default=True), sg.Radio('Trapezoid', 'METHOD'), sg.Radio('Simpson', 'METHOD')],
                [sg.Checkbox('Detailed report')],
                [sg.Button('SOLVE'), sg.Text('Result :', border_width=5) , sg.Text('Empty', size=(50,1), key='_result_')] 
            ]
        self.formulasUsedLayout = [
            [sg.Image('formula_1.png')],
            [sg.Image('formula_2.png')],
            [sg.Image('formula_3.png')]
        ]

    def create_windows(self):
    # Create the Window
        self.window = sg.Window('Integrals solver', self.layout, icon='integral.ico', size=(380,180))
        self.formulasWindow = sg.Window('FORMULAS USED', self.formulasUsedLayout, icon='integral.ico', size=(500,320))
    
    def get_windows(self):
        self.create_windows()
        return (self.window, self.formulasWindow)

    def read(self):
        return self.window.read()

    def close(self):
        return self.window.close()

class Handler:

    def __init__(self, *window):
        self.window = window
        print(window)

    def setState(self, state):
        self.state = state

    def setValues(self, values):
        self.values = values

    def state_machine(self):
        
        if self.state == 'SOLVE':
            self.solve_st()

        elif self.state in (None, 'Exit'):
            exit()
        elif self.state == 'About...':
            sg.Popup('Integral calculation app by Pavlo Chaikovskyi 125B')  
        elif self.state == 'Formulas used':
            self.window[1].read()
        elif self.state == 'Help':
            sg.Popup('HELPER', 'Into "A" field enter upper limit\nInto "B" field enter lower limit\nAnd into expression - enter your function\nlike - x**2\nIf you want detailed result\nwith memory usag and time - \nclick certain checkbox')

    def solve_st(self):
        if '' not in self.values.values():
            if self.values[3] == True:
                method = 'Rectangle method'
            elif self.values[4] == True:
                method = 'Trapezoid method'
            elif self.values[5] == True:
                method = 'Simpson method'
            result = integral.processArguments([self.values[1], self.values[2], self.values[3]], method)
            if self.values[7] == True:
                sg.Popup(f'RESULT: {result[0]}', result[1], result[2])
            else:
                self.window[0].Element('_result_').Update(str(result[0]))
        else:
            sg.Popup('Opps!', 'One of the fields is empty.')