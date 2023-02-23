run:
	cls
	@powershell write-host -fore Yellow Starting Software with Pythonscript...
	@pyside6-uic .\res\mainui.ui > .\res\ui_mainui.py
	@pyside6-uic .\res\splashui.ui > .\res\ui_splashui.py
	@pyside6-rcc ressource.qrc > ressource_rc.py
	@python main.py

test:
	cls
	@powershell write-host -fore Yellow Starting Testprocess...
	@pytest
	@powershell write-host -fore Green Testprocess successfully finished!

build:
	cls
	@powershell write-host -fore Yellow Starting buildprocess..
	@pyside6-uic .\res\mainui.ui > .\res\ui_mainui.py
	@pyside6-uic .\res\splashui.ui > .\res\ui_splashui.py
	@pyside6-rcc ressource.qrc > ressource_rc.py
	@pyinstaller .\config\main.spec --noconfirm
	@C:\Program Files (x86)\solicus\InstallForge\bin\ifbuilderenvx86.exe

clean:
	cls
	@powershell write-host -fore Yellow Cleanup Projectfiles...
	@if exist "./build" rd /s /q build
	@if exist "./dist" rd /s /q dist
	@if exist "./res/__pycache__" rd /s /q .\res\__pycache__
	@if exist "./tests/__pycache__" rd /s /q .\tests\__pycache__
	@if exist "__pycache__" rd /s /q .\__pycache__
	@if exist ".pytest_cache" rd /s /q .pytest_cache
	@if exist "./data/mo.key" del /s /q .\data\mo.key
	@powershell write-host -fore Green Cleanup finished!