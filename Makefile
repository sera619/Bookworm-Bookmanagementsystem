run:
	pyside6-uic .\res\mainui.ui > .\res\ui_mainui.py
	pyside6-uic .\res\splashui.ui > .\res\ui_splashui.py
	pyside6-rcc ressource.qrc > ressource_rc.py
	python main.py

test:
	pytest

build:
	pyside6-uic .\res\mainui.ui > .\res\ui_mainui.py
	pyside6-uic .\res\splashui.ui > .\res\ui_splashui.py
	pyside6-rcc ressource.qrc > ressource_rc.py
	pyinstaller .\config\main.spec --noconfirm

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./res/__pycache__" rd /s /q .\res\__pycache__
	if exist "./tests/__pycache__" rd /s /q .\tests\__pycache__
	if exist "__pycache__" rd /s /q .\__pycache__
	if exist ".pytest_cache" rd /s /q .pytest_cache