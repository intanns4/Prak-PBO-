import pygame
import sys

# Inheritance (inheritance dari pygame.sprite.Sprite)
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Encapsulation (menggunakan setter dan getter)
    def set_text(self, text, font, color):
        self.text = font.render(text, True, color)
        text_rect = self.text.get_rect(center=self.rect.center)
        self.image.blit(self.text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 350))
        pygame.display.set_caption('Tic Tac Toe')
        self.clock = pygame.time.Clock()

        # Abstraction (membuat fungsi untuk memulai game)
        self.init_game()

    def init_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.game_over = False

        self.font = pygame.font.Font(None, 48)
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = Button(col * 100, row * 100, 100, 100, (255, 255, 255))
                self.buttons.add(button)

    def draw_board(self):
        self.screen.fill((0, 0, 255))
        for button in self.buttons:
            self.screen.blit(button.image, button.rect)

    def check_win(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        # Check for tie
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Tie'
        return None

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.is_clicked(pos) and self.board[button.rect.y // 100][button.rect.x // 100] == ' ':
                            self.board[button.rect.y // 100][button.rect.x // 100] = self.turn
                            self.turn = 'O' if self.turn == 'X' else 'X'
                            winner = self.check_win()
                            if winner:
                                self.game_over = True
                            break
                if self.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.init_game()

            self.draw_board()
            for row in range(3):
                for col in range(3):
                    text = self.font.render(self.board[row][col], True, (0, 0, 0))
                    self.screen.blit(text, (col * 100 + 40, row * 100 + 40))

            if self.game_over:
                if winner == 'Tie':
                    text = self.font.render('Tie!', True, (255, 255, 255))
                else:
                    text = self.font.render(f'{winner} wins!', True, (255, 255, 255))
                self.screen.blit(text, (50, 300))
                restart_text = self.font.render('Press SPACE to restart', True, (255, 255, 255))
                self.screen.blit(restart_text, (20, 330))

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == '__main__':
    game = TicTacToe()
    game.run_game()
