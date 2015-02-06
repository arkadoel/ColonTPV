import platform
import sys

def run_wpf_gui():
    import wpf

    from System.Windows import Application, Window
    from gui.windows.MainWindow import MainWindow

    Application().Run(MainWindow())

def run_qt_gui():
    pass

def detect_system_and_run():
    '''
    Detectar el sistema operativo y arrancar la aplicacion
    con una interfaz WPF o una QT
    '''
    if platform.python_implementation().lower() == 'ironpython':
        if platform.system() == 'cli':
            #estamos en windows bajo ironpython
            run_wpf_gui()
        else:
            #estamos en linux ejecutando mono-ironpython
            pass
    else:
        #para otros sistemas operativos implementar QT
        run_qt_gui()

if __name__ == '__main__':
    detect_system_and_run()

