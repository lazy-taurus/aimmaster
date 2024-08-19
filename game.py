import math
import random
import time
import pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Create the display window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Master")

# Constants
TARGET_INTERVAL = 400  # Time in milliseconds to add a new target
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30  # Padding from the window edges

BACKGROUND_COLOR = (0, 25, 40)
LIVES_COUNT = 3
TOP_BAR_HEIGHT = 50

FONT = pygame.font.SysFont("comicsans", 24)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    PRIMARY_COLOR = "red"
    SECONDARY_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.growing = True

    def update(self):
        # Toggle growth/shrink based on max size
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.growing = False
        if self.growing:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        # Draw target with concentric circles
        pygame.draw.circle(win, self.PRIMARY_COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECONDARY_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.PRIMARY_COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECONDARY_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        # Check if the mouse click is within the target
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        return distance <= self.size

def draw_targets(win, targets):
    # Fill the window with background color and draw targets
    win.fill(BACKGROUND_COLOR)
    for target in targets:
        target.draw(win)

def format_time(seconds):
    milliseconds = math.floor(int(seconds * 1000 % 1000) / 100)
    sec = int(round(seconds % 60, 1))
    min = int(seconds // 60)
    return f"{min:02d}:{sec:02d}.{milliseconds}"

def draw_status_bar(win, elapsed, hits, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = FONT.render(f"Time: {format_time(elapsed)}", 1, "black")
    speed = round(hits / elapsed, 1)
    speed_label = FONT.render(f"Speed: {speed} t/s", 1, "black")
    hits_label = FONT.render(f"Hits: {hits}", 1, "black")
    lives_label = FONT.render(f"Lives: {LIVES_COUNT - misses}", 1, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))

def display_end_screen(win, elapsed, hits, clicks):
    win.fill(BACKGROUND_COLOR)
    time_label = FONT.render(f"Time: {format_time(elapsed)}", 1, "white")
    speed = round(hits / elapsed, 1)
    speed_label = FONT.render(f"Speed: {speed} t/s", 1, "white")
    hits_label = FONT.render(f"Hits: {hits}", 1, "white")
    accuracy = round(hits / clicks * 100, 1)
    accuracy_label = FONT.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (center_position(time_label), 100))
    win.blit(speed_label, (center_position(speed_label), 200))
    win.blit(hits_label, (center_position(hits_label), 300))
    win.blit(accuracy_label, (center_position(accuracy_label), 400))

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()

def center_position(surface):
    return WIDTH / 2 - surface.get_width() / 2

def main():
    running = True
    targets = []
    clock = pygame.time.Clock()

    hits = 0
    total_clicks = 0
    missed = 0
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INTERVAL)

    while running:
        clock.tick(60)
        mouse_clicked = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                total_clicks += 1

        for target in targets:
            target.update()
            if target.size <= 0:
                targets.remove(target)
                missed += 1
            if mouse_clicked and target.collide(*mouse_pos):
                targets.remove(target)
                hits += 1

        if missed >= LIVES_COUNT:
            display_end_screen(WINDOW, elapsed_time, hits, total_clicks)

        draw_targets(WINDOW, targets)
        draw_status_bar(WINDOW, elapsed_time, hits, missed)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
