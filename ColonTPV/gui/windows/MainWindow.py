import wpf

from System.Windows import *
import gui.windows
from gui.windows.MenuPrincipal import MenuPrincipal

class MainWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, './gui/windows/MainWindow.xaml')
        self.Title = 'Colon TPV'

        #forzando tam para que no den la lata
        self.Width = gui.windows.MIN_WINDOW_WIDTH
        self.Height = gui.windows.MIN_WINDOW_HEIGHT
        self.visorAdaptable.Width = self.Width
        self.visorAdaptable.Height = self.Height
        self.Controles.Width = self.Width
        self.Controles.Height = self.Height

        menu_principal = MenuPrincipal()
        #menu_principal.Margin.Left = 0
        #menu_principal.Margin.Right = 0
        self.Controles.Children.Add(menu_principal)
        

