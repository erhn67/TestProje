del/Q C:\Apps\PythonTry1\MainWindow.ui
del/Q C:\Apps\PythonTry1\Resources.qrc

copy C:\Apps\qt1\proj1\MainWindow.ui C:\Apps\PythonTry1\.
copy C:\Apps\qt1\proj1\Resources.qrc C:\Apps\PythonTry1\.

pyuic5 MainWindow.ui -o MainWindow.py
pyrcc5 -o C:\Apps\PythonTry1\Resources_rc.py C:\Apps\PythonTry1\Resources.qrc
