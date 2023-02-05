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
	if exists "./build" rd /s /q build
	if exists "./dist" rd /s /q dist