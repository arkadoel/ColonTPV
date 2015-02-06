import wpf

from System.Windows import Window

class MainWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'gui/windows/MainWindow.xaml')
