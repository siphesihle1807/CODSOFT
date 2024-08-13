import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QStackedWidget, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

class StartPage(QWidget):
    def __init__(self, stack_widget):
        super().__init__()
        self.stack_widget = stack_widget

        # Set up the layout
        self.layout = QVBoxLayout()

        # Add label and start button
        self.label = QLabel("Welcome to Rock Paper Scissors!")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.startButton = QPushButton("Start Game")
        self.startButton.clicked.connect(self.startGame)
        self.layout.addWidget(self.startButton, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def startGame(self):
        self.stack_widget.setCurrentIndex(1)

class RockPaperScissorsGame(QWidget):
    def __init__(self, stack_widget):
        super().__init__()
        self.stack_widget = stack_widget

        # Set up the UI
        self.setWindowTitle('Rock Paper Scissors')
        self.setGeometry(300, 300, 400, 300)

        # Main layout
        self.layout = QVBoxLayout()

        # Label to display instructions
        self.label = QLabel("Let's play a game...\nHere are your choices:")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Grid layout for buttons and score
        self.gridLayout = QGridLayout()

        # Fixed icon size
        icon_size = QSize(100, 100)

        # Rock button
        self.rockButton = QPushButton()
        self.rockButton.setIcon(QIcon(QPixmap('rock.svg')))
        self.rockButton.setIconSize(icon_size)
        self.rockButton.clicked.connect(lambda: self.playGame(0))
        self.gridLayout.addWidget(self.rockButton, 0, 0)

        # Paper button
        self.paperButton = QPushButton()
        self.paperButton.setIcon(QIcon(QPixmap('document-documents-paper-clip.svg')))
        self.paperButton.setIconSize(icon_size)
        self.paperButton.clicked.connect(lambda: self.playGame(1))
        self.gridLayout.addWidget(self.paperButton, 0, 1)

        # Scissors button
        self.scissorsButton = QPushButton()
        self.scissorsButton.setIcon(QIcon(QPixmap('scissors.svg')))
        self.scissorsButton.setIconSize(icon_size)
        self.scissorsButton.clicked.connect(lambda: self.playGame(2))
        self.gridLayout.addWidget(self.scissorsButton, 0, 2)

        self.layout.addLayout(self.gridLayout)

        # Labels to display player and computer choices
        self.playerChoiceLabel = QLabel("Your choice: ")
        self.layout.addWidget(self.playerChoiceLabel)

        self.computerChoiceLabel = QLabel("Computer's choice: ")
        self.layout.addWidget(self.computerChoiceLabel)

        # Label to display the result
        self.resultLabel = QLabel("")
        self.layout.addWidget(self.resultLabel)

        # Scoreboard
        self.scoreLabel = QLabel("Score - You: 0 | Computer: 0 | Ties: 0")
        self.layout.addWidget(self.scoreLabel)
        self.playerScore = 0
        self.computerScore = 0
        self.ties = 0

        # Set the layout to the main window
        self.setLayout(self.layout)

    def playGame(self, player_choice):
        # Update player choice label
        choices = ["Rock", "Paper", "Scissors"]
        choice_images = ['rock.svg', 'document-documents-paper-clip.svg', 'scissors.svg']
        self.playerChoiceLabel.setText(f"Your choice: {choices[player_choice]}")
        self.playerChoiceLabel.setPixmap(self.scalePixmap(choice_images[player_choice]))

        # Generate computer choice
        comp_choice = random.randint(0, 2)
        self.computerChoiceLabel.setText(f"Computer's choice: {choices[comp_choice]}")
        self.computerChoiceLabel.setPixmap(self.scalePixmap(choice_images[comp_choice]))

        # Determine the winner
        if player_choice == comp_choice:
            self.resultLabel.setText("It's a tie!")
            self.ties += 1
        elif (player_choice == 0 and comp_choice == 2) or \
                (player_choice == 1 and comp_choice == 0) or \
                (player_choice == 2 and comp_choice == 1):
            self.resultLabel.setText("Congratulations, you win!")
            self.playerScore += 1
        else:
            self.resultLabel.setText("The computer wins!")
            self.computerScore += 1

        self.updateScoreboard()
        self.checkEndGame()

    def scalePixmap(self, path):
        """Helper function to scale the QPixmap to a fixed size"""
        pixmap = QPixmap(path)
        return pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)

    def updateScoreboard(self):
        self.scoreLabel.setText(f"Score - You: {self.playerScore} | Computer: {self.computerScore} | Ties: {self.ties}")

    def checkEndGame(self):
        if self.playerScore == 5 or self.computerScore == 5:
            if self.playerScore > self.computerScore:
                final_result = "You won the game!"
                winner_image = 'user.svg'
            else:
                final_result = "The computer won the game!"
                winner_image = 'monitor.svg'
            self.stack_widget.widget(2).updateResult(final_result, winner_image)
            self.stack_widget.setCurrentIndex(2)

    def resetGame(self):
        self.playerScore = 0
        self.computerScore = 0
        self.ties = 0
        self.updateScoreboard()
        self.resultLabel.setText("")
        self.playerChoiceLabel.setText("Your choice: ")
        self.computerChoiceLabel.setText("Computer's choice: ")

class EndPage(QWidget):
    def __init__(self, stack_widget):
        super().__init__()
        self.stack_widget = stack_widget

        self.layout = QVBoxLayout()

        self.resultLabel = QLabel("")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.resultLabel)

        self.winnerImage = QLabel()
        self.winnerImage.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.winnerImage)

        self.playAgainButton = QPushButton("Play Again")
        self.playAgainButton.clicked.connect(self.playAgain)
        self.layout.addWidget(self.playAgainButton, alignment=Qt.AlignCenter)

        self.exitButton = QPushButton("Exit")
        self.exitButton.clicked.connect(self.exitGame)
        self.layout.addWidget(self.exitButton, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def updateResult(self, result, image_path):
        self.resultLabel.setText(result)
        pixmap = QPixmap(image_path)
        self.winnerImage.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

    def playAgain(self):
        game_page = self.stack_widget.widget(1)  # Get the game page
        game_page.resetGame()  # Reset the game scores and UI
        self.stack_widget.setCurrentIndex(0)  # Go back to the start page

    def exitGame(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the stack widget
    stack_widget = QStackedWidget()

    # Create instances of the pages
    start_page = StartPage(stack_widget)
    game_page = RockPaperScissorsGame(stack_widget)
    end_page = EndPage(stack_widget)

    # Add pages to the stack widget
    stack_widget.addWidget(start_page)
    stack_widget.addWidget(game_page)
    stack_widget.addWidget(end_page)

    # Set the initial page
    stack_widget.setCurrentIndex(0)

    # Show the stack widget
    stack_widget.setWindowTitle('Rock Paper Scissors')
    stack_widget.setGeometry(300, 300, 400, 300)
    stack_widget.show()

    sys.exit(app.exec_())

