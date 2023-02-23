from PySide6 import *


class ButtonStyles:
    NormalButton = """
    QPushButton{
	border: 1px solid rgba(170, 0, 0,165);
	padding: 2px 20px;
	border-radius: 2%;
	color: rgb(255, 0, 0)
}

QPushButton::Hover{
	border: 1.2px solid rgb(255, 0, 0);
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));
	
}

QPushButton::Pressed{
	border: 1.4px solid;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));
	border-color: rgb(255, 0, 0);
	color: #FFF;
}
    """
    
    MenuButton = """
        QPushButton{
	border: 1px solid rgba(170, 0, 0,165);
	padding: 2px 20px;
	border-radius: 2%;
	color: rgb(255, 0, 0)
}

QPushButton::Hover{
	border: 1.2px solid rgb(255, 0, 0);
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));
	
}

QPushButton::Pressed{
	border: 1.4px solid;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));
	border-color: rgb(255, 0, 0);
	color: #FFF;
}
    
    QPushButton::Focus{
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));
	border: 1.4px solid rgb(255, 0, 0);
	color: #FFF;
}
    """

class TextStyles:
    InformationText = """
    QLabel{
	font: 12px "Ethnocentric";
	color: rgb(170, 0, 0);
}"""

    SubHeaderText = """
    QLabel{
		font: 26pt "Ethnocentric";
}"""