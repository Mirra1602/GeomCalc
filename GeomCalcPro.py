import wx
import shape
import  cStringIO
import matplotlib
#matplotlib.use('TkAgg')
#matplotlib.use('WXAgg')
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure


class MyGUI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Rad Geometry', size = (400, 300))
         
### Add a panel so it looks correct on all platforms
         
        self.panel = wx.Panel(self, wx.ID_ANY)

        labelShape = wx.StaticText(self.panel, wx.ID_ANY, 'Shape:')
        self.ListShape = ['','Triangle', 'Right Triangle','Parallelolograpm', 'Rectangle', 'Rhombus', 'Square', 'Circle']
        self.ch1 = wx.Choice(self.panel, wx.ID_ANY, choices = self.ListShape)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice1, self.ch1)

        labelUnknown = wx.StaticText(self.panel, wx.ID_ANY, 'Uknown:')
        self.ListUnknown = ['']
        self.ch2 = wx.Choice(self.panel, wx.ID_ANY, choices = self.ListUnknown)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.ch2)

        labelInput = wx.StaticText(self.panel, wx.ID_ANY, 'Input:')
         
        self.labelA = wx.StaticText(self.panel, wx.ID_ANY, 'a')
        self.inputA = wx.TextCtrl(self.panel, wx.ID_ANY, '')
 
        self.labelB = wx.StaticText(self.panel, wx.ID_ANY, 'b')
        self.inputB = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        self.labelAngle = wx.StaticText(self.panel, wx.ID_ANY, u'angle \u03B1')
        self.inputAngle = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        self.labelradius = wx.StaticText(self.panel, wx.ID_ANY, 'r')
        self.inputradius = wx.TextCtrl(self.panel, wx.ID_ANY, '')

### add a button:
        Btn = wx.Button(self.panel, wx.ID_ANY, 'Push for Unknown')
        self.Bind(wx.EVT_BUTTON, self.onPush, Btn)

        Btn2 = wx.Button(self.panel, wx.ID_ANY, 'Draw Shape')
        self.Bind(wx.EVT_BUTTON, self.onPush2, Btn2)

### add output:        
        labelFormula = wx.StaticText(self.panel, wx.ID_ANY, 'Formula:')
        labelResult = wx.StaticText(self.panel, wx.ID_ANY, 'Result:')
 



### do the layout
        mainSizer        = wx.BoxSizer(wx.VERTICAL)
        inputOneSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFiveSizer = wx.BoxSizer(wx.HORIZONTAL)


  
### add the widgets to the layout
        inputOneSizer.Add(labelShape, 0, wx.ALL, 5)
        inputOneSizer.Add(self.ch1, 1, wx.ALL|wx.EXPAND, 3)
 
        inputOneSizer.Add(labelUnknown, 0, wx.ALL, 5)
        inputOneSizer.Add(self.ch2, 1, wx.ALL|wx.EXPAND, 5)

### make an instance; so I can modify
        self.inputThreeSizer = inputThreeSizer
        inputThreeSizer.Add(labelInput, 0, wx.ALL|wx.EXPAND, 5)
 
        inputThreeSizer.Add(self.labelA, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputA, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(self.labelB, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputB, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(self.labelAngle, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputAngle, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(self.labelradius, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputradius, 1, wx.ALL|wx.EXPAND, 5)

        btnSizer.Add(Btn, 0, wx.ALL, 5)
        btnSizer.Add(Btn2, 0, wx.ALL, 5)

### output, Formula and Result
        inputFourSizer.Add(labelFormula, 0, wx.ALL, 5)
        self.outFormula = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        inputFiveSizer.Add(labelResult, 0, wx.ALL, 5)
        self.outResult = wx.TextCtrl(self.panel, style=wx.TE_READONLY)


### set up the order of widgets in the layout 
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)


        mainSizer.Add(inputThreeSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        
        mainSizer.Add(inputFourSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.outFormula, 0, wx.GROW | wx.ALL, 4)

        mainSizer.Add(inputFiveSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.outResult, 0, wx.GROW | wx.ALL, 4)
        # mainSizer.Add(self.outBox, 0, wx.ALL | wx.GROW, sizer = (10, 10))

        self.panel.SetSizer(mainSizer)
        mainSizer.Fit(self)

        


### Hides and unhides input options based on shape Selection
### ch2 controls Unknown options-needed to vary because of Circle
### ch2.Clear to clear previous options and prevent from keep adding 
### elements; '' needed as first to force the user to make a selection
### (otherwise) Selection does not register input
    def EvtChoice1(self, event):
        if event.Selection == 1:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter') 
            self.inputThreeSizer.Show(self.labelA)
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Show(self.labelB)
            self.inputThreeSizer.Show(self.inputB)
            self.inputThreeSizer.Show(self.labelAngle)
            self.inputThreeSizer.Show(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)
        elif event.Selection == 2:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter') 
            self.inputThreeSizer.Show(self.labelA)
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Show(self.labelB)
            self.inputThreeSizer.Show(self.inputB)
            self.inputThreeSizer.Hide(self.labelAngle)
            self.inputThreeSizer.Hide(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)
        elif event.Selection == 3:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter')
            self.inputThreeSizer.Show(self.labelA)
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Show(self.labelB)
            self.inputThreeSizer.Show(self.inputB)
            self.inputThreeSizer.Show(self.labelAngle)
            self.inputThreeSizer.Show(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)            
        elif event.Selection == 4:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter')
            self.inputThreeSizer.Show(self.labelA)
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Show(self.labelB)
            self.inputThreeSizer.Show(self.inputB)
            self.inputThreeSizer.Hide(self.labelAngle)
            self.inputThreeSizer.Hide(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)            
        elif event.Selection == 5:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter')
            self.inputThreeSizer.Show(self.labelA)
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Hide(self.labelB)
            self.inputThreeSizer.Hide(self.inputB)
            self.inputThreeSizer.Show(self.labelAngle)
            self.inputThreeSizer.Show(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)
        elif event.Selection == 6:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Perimeter')
            self.inputThreeSizer.Show(self.inputA)
            self.inputThreeSizer.Hide(self.labelB)
            self.inputThreeSizer.Hide(self.inputB)
            self.inputThreeSizer.Hide(self.labelAngle)
            self.inputThreeSizer.Hide(self.inputAngle)
            self.inputThreeSizer.Hide(self.labelradius)
            self.inputThreeSizer.Hide(self.inputradius)            
        elif event.Selection == 7:
            self.ch2.Clear()
            self.ch2.Append('')
            self.ch2.Append('Area')
            self.ch2.Append('Circumferance')
            self.inputThreeSizer.Hide(self.labelA)
            self.inputThreeSizer.Hide(self.inputA)
            self.inputThreeSizer.Hide(self.labelB)
            self.inputThreeSizer.Hide(self.inputB)
            self.inputThreeSizer.Hide(self.labelAngle)
            self.inputThreeSizer.Hide(self.inputAngle)
            self.inputThreeSizer.Show(self.labelradius)
            self.inputThreeSizer.Show(self.inputradius)
        return self.ch1.Selection



    def EvtChoice2(self, event):
        return self.ch2.Selection


### declare event that happen on push
    def onPush(self, evt=None):

### grab the input parameters from the TxtCtrl
### inputs are not alwats present do set them to 0
### otherwise the program crashes when Classes are initialized in 
### option 1
        if self.inputA.Value:
            a = int(self.inputA.Value)
        else:
            a = 0.1
        if self.inputB.Value:
            b = int(self.inputB.Value)
        else:
            b = 0.1
        if self.inputAngle.Value:
            angle = int(self.inputAngle.Value)
        else:
            angle = 0.1
        if self.inputradius.Value:
            r = int(self.inputradius.Value)
        else:
            r = 0.1


### Pop up if .Selection is 0(no selection made)
### if Triangle is the first position and shows in the window without being selecting then 
### .Selection does not register; if user clicked on the dropdown and still 
### chose the "empty" choice a pop up warning will be displayed
        if self.ch1.Selection==0 or self.ch2.Selection==0:
            dlg = wx.MessageDialog(self, "Choose Shape and Unknown", "You did not make a selection",wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()

### create a dictionary to connect the choice selection to the proper Class
### also pass the input to initialize
        option1 = { 1 : shape.Triangle(a,b,angle),
                    2 : shape.Right_Triangle(a,b),
                    3 : shape.Parallelogram(a,b,angle),
                    4 : shape.Rectangle(a,b),
                    5 : shape.Rhombus(a, angle),
                    6 : shape.Square(a),
                    7 : shape.Circle(r)
                    }
        get_shape = option1[self.ch1.Selection] ### create a class object 

### create a dictionary for the second choice selection 
### and access it with the class object
### need to separate the circle methods and all other since methods' names differ
### (perimeter/circumferance)
### also sets the Formula output       
        if self.ch1.Selection == 7 :
            option2 = { 1 : self.get_shape.area,
                        2 : self.get_shape.circumferance}
            if self.ch2.Selection == 1:
                self.outFormula.Value = self.get_shape.area_formula
            else: 
                self.outFormula.Value = self.get_shape.circumferance_formula
        else:
            option2 = { 1 : self.get_shape.area,
                        2 : self.get_shape.perimeter}
            if self.ch2.Selection == 1:
                self.outFormula.Value = self.get_shape.area_formula
            else: 
                self.outFormula.Value = self.get_shape.perimeter_formula


### Output result based on Selections        
        self.outResult.Value = str(option2[self.ch2.Selection])



### Pop a warning if angle is invalid 
        if angle > 180 or angle <= 0:
            dlg = wx.MessageDialog(self, "Angle has to be less than 180", 
               "Sum of the angles of a tirangle is equal to 180",wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
### Pop up warning if input values are invalid
        if a <= 0 or b <= 0 or r<=0:
            dlg = wx.MessageDialog(self, "Invalid Input", 
               "Only positive input values. Length cannot be 0 or negative",wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()

    def onPush2(self, evt=None):
        if self.inputA.Value:
            a = int(self.inputA.Value)
        else:
            a = 0.1
        if self.inputB.Value:
            b = int(self.inputB.Value)
        else:
            b = 0.1
        if self.inputAngle.Value:
            angle = int(self.inputAngle.Value)
        else:
            angle = 0.1
        if self.inputradius.Value:
            r = int(self.inputradius.Value)
        else:
            r = 0.1


        if self.ch1.Selection==0 or self.ch2.Selection==0:
            dlg = wx.MessageDialog(self, "Choose Shape and Unknown", "You did not make a selection",wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()

        option1 = { 1 : shape.Triangle(a,b,angle),
                    2 : shape.Right_Triangle(a,b),
                    3 : shape.Parallelogram(a,b,angle),
                    4 : shape.Rectangle(a,b),
                    5 : shape.Rhombus(a, angle),
                    6 : shape.Square(a),
                    7 : shape.Circle(r)
                    }
        get_shape = option1[self.ch1.Selection] ### create a class object 
        get_shape.draw()
        # self.canvas = FigureCanvas(self, -1, self.figure)
        # self.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        # self.SetSizer(self.sizer)
        # self.Fit()




### clear the input boxes at the end of the run; 
        self.inputA.Clear()
        self.inputB.Clear()
        self.inputAngle.Clear()
        self.inputradius.Clear()





    def closeProgram(self):
        self.Close()

if __name__ == '__main__':
    #app = wx.PySimpleApp()
    app = wx.App()
    frame = MyGUI().Show()
    app.MainLoop()



