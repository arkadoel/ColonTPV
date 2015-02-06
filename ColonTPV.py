import platform
import sys

def detect_system_and_run():
    if platform.python_implementation().lower() == 'ironpython':
        if platform.system() == 'cli':
            #estamos en windows bajo ironpython
            import wpf

            from System.Windows import Application, Window
            from gui.windows.MainWindow import MainWindow

            Application().Run(MainWindow())
        else:
            #estamos en linux ejecutando mono
            pass
    else:
        #para otros sistemas operativos implementar QT
        pass

if __name__ == '__main__':
    detect_system_and_run()

