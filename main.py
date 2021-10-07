# Module Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys

# File imports
from assets import Assets

WINDOW_TITLE = "Rock Paper Scissors"

WIDTH, HEIGHT = 640, 480

ATTRIBUTION = open("attribution.txt").read()

FONT_SIZE = 20


def choose_random_icon() -> QtGui.QIcon:
    icons = [Assets.rock, Assets.paper, Assets.scissors]
    return QtGui.QIcon(random.choice(icons))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.central_widget = None
        self.font = None
        self.background = None

        self.rock_button = None
        self.paper_button = None
        self.scissors_button = None

        self.user_input = None
        self.computer_input = None

        self.attribution_button = None

        self._translate = QtCore.QCoreApplication.translate

    def resizeEvent(self, event) -> None:
        print(self.width(), self.height())
        self.background.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))

    #     self.rock_button.setGeometry(QtCore.QRect(padding, 40, 160, 160))
    #     self.paper_button.setGeometry(QtCore.QRect((padding * 2) + 160, 40, 160, 160))
    #     self.scissors_button.setGeometry(QtCore.QRect((padding * 3) + 320, 40, 160, 160))
    #     self.user_input.setGeometry(QtCore.QRect(padding, 240, 160, 160))
    
        self.attribution_button.setGeometry(QtCore.QRect(self.width() - 80, self.height() - 30, 75, 25))

    def setup_ui(self, main_window) -> None:
        """Configure UI"""
        main_window.setObjectName("main_window")

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setMinimumSize(WIDTH, HEIGHT)
        self.central_widget.setObjectName("centralwidget")

        # Font Object
        self.font = QtGui.QFont()
        self.font.setPointSize(FONT_SIZE)

        # Set Background Colour
        self.background = QtWidgets.QLabel(self.central_widget)
        self.background.setGeometry(0, 0, WIDTH, HEIGHT)
        self.background.setPixmap(QtGui.QPixmap(Assets.background))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        # Rock Button Object
        self.rock_button = QtWidgets.QPushButton(self.central_widget)
        self.rock_button.setGeometry(QtCore.QRect(40, 40, 160, 160))
        self.rock_button.clicked.connect(self.on_rock)
        self.rock_button.setObjectName("rock_button")
        self.rock_button.setStyleSheet("""
        QPushButton {
            border-radius: 20px;
            background: url(Assets/rock.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)

        # Paper Button Object
        self.paper_button = QtWidgets.QPushButton(self.central_widget)
        self.paper_button.setGeometry(QtCore.QRect(240, 40, 160, 160))
        self.paper_button.clicked.connect(self.on_paper)
        self.paper_button.setObjectName("paper_button")
        self.paper_button.setStyleSheet("""
        QPushButton {
            border-radius: 20px;
            background: url(Assets/paper.jpg);
            background-color: rgb(255, 255, 255);s
        }
        """)

        # Scissors Button Object
        self.scissors_button = QtWidgets.QPushButton(self.central_widget)
        self.scissors_button.setGeometry(QtCore.QRect(440, 40, 160, 160))
        self.scissors_button.clicked.connect(self.on_scissors)
        self.scissors_button.setObjectName("scissors_button")
        self.scissors_button.setStyleSheet("""
        QPushButton {
            border-radius: 20px;
            background: url(Assets/scissors.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)

        # Player Input
        self.user_input = QtWidgets.QLabel(self.central_widget)
        self.user_input.setGeometry(QtCore.QRect(40, 240, 160, 160))
        self.user_input.setFont(self.font)
        self.user_input.setObjectName("user_input")
        self.user_input.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background: url(Assets/rock.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)

        # Computer Input
        self.computer_input = QtWidgets.QLabel(self.central_widget)
        self.computer_input.setGeometry(QtCore.QRect(240, 240, 160, 160))
        self.computer_input.setFont(self.font)
        self.computer_input.setObjectName("computer_input")
        self.computer_input.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background: url(Assets/rock.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)

        # Output Box
        self.font.setPointSize(15)
        self.output = QtWidgets.QLabel(self.central_widget)
        self.output.setGeometry(QtCore.QRect(440, 240, 160, 60))
        self.output.setFont(self.font)
        self.output.setObjectName("output")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background-color: rgb(255, 255, 255);
        }
        """)

        # Attribution Button
        self.font.setPointSize(10)
        self.attribution_button = QtWidgets.QPushButton(self.central_widget)
        self.attribution_button.setGeometry(QtCore.QRect(560, 450, 75, 25))
        self.attribution_button.setFont(self.font)
        self.attribution_button.clicked.connect(self.on_attribute)
        self.attribution_button.setObjectName("attribution_button")  
        self.font.setPointSize(FONT_SIZE)

        main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(main_window)

    def retranslate_ui(self, main_window) -> None:
        main_window.setWindowTitle(self._translate("main_window", WINDOW_TITLE))
        main_window.setWindowIcon(choose_random_icon())

        self.attribution_button.setText(self._translate("main_window", "Attribution"))

    @staticmethod
    def parse_inputs(user: int, computer: int) -> str:
        choices = {
            0 : "rock",
            1 : "paper",
            2 : "scissors",
        }

        user = choices[user]
        computer = choices[computer]

        if user == "rock":
            if computer == "rock":
                return "draw"

            elif computer == "paper":
                return "computer wins"

            elif computer == "scissors":
                return "you win"
        elif user == "paper":
            if computer == "rock":
                return "you win"

            elif computer == "paper":
                return "draw"

            elif computer == "scissors":
                return "computer wins"
        elif user == "scissors":
            if computer == "rock":
                return "computer wins"
            
            elif computer == "paper":
                return "you win"

            elif computer == "scissors":
                return "draw"


    @staticmethod
    def on_attribute() -> None:
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowIcon(QtGui.QIcon(Assets.info_icon))
        msg_box.setWindowTitle("Credits")
        msg_box.setText(ATTRIBUTION)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def generate_computer_input(self):
        choices =  ["rock.jpg", "paper.jpg", "scissors.jpg"]
        self.computer_choice = random.randint(0, 2999) % 3


        style_sheet = "\n".join([
            "QLabel {",
            "    border-radius: 20px;",
           f"    background: url(Assets/{choices[self.computer_choice]});",
            "    background-color: rgb(255, 255, 255);"
            "}"        
        ])

        self.computer_input.setStyleSheet(style_sheet)

        self.output.setText(self.parse_inputs(self.user_choice, self.computer_choice))

    def on_rock(self) -> None:
        self.user_input.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background: url(Assets/rock.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)
        self.user_choice = 0

        self.generate_computer_input()

    def on_paper(self) -> None:
        self.user_input.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background: url(Assets/paper.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)
        self.user_choice = 1

        self.generate_computer_input()

    def on_scissors(self) -> None:
        self.user_input.setStyleSheet("""
        QLabel {
            border-radius: 20px;
            background: url(Assets/scissors.jpg);
            background-color: rgb(255, 255, 255);
        }
        """)
        self.user_choice = 2

        self.generate_computer_input()


def main():
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.setup_ui(ui)
    ui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
