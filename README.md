## AimMaster - Aim Trainer Game

**AimMaster** is an engaging and challenging aim trainer game designed to improve your targeting skills. Perfect for gamers and anyone looking to enhance their precision and reaction time, AimMaster provides an interactive way to practice your aim in a fun and competitive environment.

### Features

- **Dynamic Targets:** Targets grow and shrink, adding variability to each session.
- **Lives System:** Manage your lives wisely as missed targets will cost you.
- **Speed Tracking:** Monitor your speed in targets per second.
- **Accuracy Metrics:** Evaluate your accuracy with detailed end-game statistics.
- **Customizable:** Enjoy a visually appealing and responsive game window with smooth controls.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/lazy-taurus/aimmaster.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd aimmaster
   ```

3. **Install Dependencies:**

   Make sure you have Python and Pygame installed. You can install the required Python packages using pip:

   ```bash
   pip install pygame
   ```

### Usage

1. **Run the Game:**

   ```bash
   python game.py
   ```

2. **Game Controls:**

   - **Mouse Click:** Shoot the targets to score points.
   - **Esc Key:** Exit the game.

3. **Game Objective:**

   Hit as many targets as you can before losing all your lives. The game tracks your speed, accuracy, and the number of targets hit.

### Code Overview

- **`Target` Class:** Manages target creation, growth, drawing, and collision detection.
- **`draw` Function:** Renders targets on the screen.
- **`draw_top_bar` Function:** Displays the game’s top bar with time, speed, hits, and lives.
- **`end_screen` Function:** Shows the final score and statistics when the game ends.
- **`main` Function:** The core game loop handles events, updates game state, and renders the game.

### Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

### Contact

For any questions or feedback, please reach out to [your email](mailto:vardanrastogi1@gmail.com).

Enjoy honing your aiming skills with AimMaster! 🚀🎯
