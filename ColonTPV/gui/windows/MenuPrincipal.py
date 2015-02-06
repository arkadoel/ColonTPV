import wpf

from System.Windows.Controls import UserControl

class MenuPrincipal(UserControl):
    def __init__(self):
        wpf.LoadComponent(self, './gui/windows/MenuPrincipal.xaml')
