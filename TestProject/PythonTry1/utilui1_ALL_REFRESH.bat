del/Q C:\Apps\PythonTry1\MainWindow.ui
del/Q C:\Apps\PythonTry1\Resources.qrc
del/F/S/Q C:\Apps\PythonTry1\Resources\.

copy C:\Apps\qt1\proj1\MainWindow.ui C:\Apps\PythonTry1\.
copy C:\Apps\qt1\proj1\Resources.qrc C:\Apps\PythonTry1\.
xcopy/E C:\Apps\qt1\proj1\Resources\*.* C:\Apps\PythonTry1\Resources\.

pyuic5 MainWindow.ui -o MainWindow.py
pyrcc5 -o C:\Apps\PythonTry1\Resources_rc.py C:\Apps\PythonTry1\Resources.qrc
