# FLAPPY BIRD CLONE

A cross-platform implementation of the classic Flappy Bird game in both Python (Pygame) and JavaScript (Phaser.js).

----------------------------------------
DESCRIPTION
----------------------------------------
This project provides two versions of the popular Flappy Bird game:
1. A Python implementation using Pygame with custom graphics and animations
2. A JavaScript implementation using Phaser.js that runs in any modern web browser

Both versions feature the core gameplay mechanics of the original Flappy Bird game,
where players navigate a bird through a series of pipes by tapping to flap the
bird's wings.

----------------------------------------
FEATURES
----------------------------------------
Python Version:
- Custom-drawn bird sprite with wing flapping animation
- Physics-based movement with realistic gravity
- Randomly generated pipes with varying gap positions
- Score tracking and high score system
- Animated clouds and environmental details
- Game over screen with restart option
- Attractive title screen with animated bird

JavaScript Version:
- Browser-based gameplay with no installation required
- Simple geometric graphics
- Physics-based movement
- Randomly generated obstacles
- Score tracking
- Game over screen with restart option

----------------------------------------
CONTROLS
----------------------------------------
Both versions:
- SPACE: Flap wings / Start game / Restart after game over

----------------------------------------
REQUIREMENTS
----------------------------------------
Python Version:
- Python 3.6+
- Pygame 2.0+

JavaScript Version:
- Any modern web browser with JavaScript enabled
- Internet connection (to load the Phaser.js library)

----------------------------------------
INSTALLATION & RUNNING
----------------------------------------
Python Version:
1. Install Python from https://python.org if not already installed
2. Install Pygame: 
   pip install pygame
3. Run the game:
   python flappy_bird.py

JavaScript Version:
1. Open the flappy_bird.html file in any web browser
   - Double-click the file
   - Or drag and drop it into your browser window

----------------------------------------
CUSTOMIZATION
----------------------------------------
Python Version:
You can modify the following constants at the top of the file:
- GRAVITY: Controls how quickly the bird falls
- FLAP_STRENGTH: Determines how high the bird jumps when flapping
- PIPE_SPEED: Sets how fast pipes move across the screen
- PIPE_SPAWN_RATE: Controls the time between pipe spawns
- PIPE_GAP: Adjusts the size of the gap between pipes

JavaScript Version:
Similar constants can be adjusted in the JavaScript code:
- GRAVITY: Controls the bird's falling speed
- FLAP_STRENGTH: Controls the bird's jump height
- PIPE_SPEED: Controls obstacle movement speed
- PIPE_SPAWN_RATE: Controls frequency of new obstacles
- PIPE_GAP: Controls the size of gaps between pipes

----------------------------------------
PROJECT STRUCTURE
----------------------------------------
flappy_bird/
├── flappy_bird.py     # Python implementation
├── flappy_bird.html   # JavaScript implementation
└── README.txt         # This file

----------------------------------------
DIFFERENCES BETWEEN VERSIONS
----------------------------------------
The Python version offers:
- More detailed graphics and animations
- High score tracking
- More visual effects and environmental details

The JavaScript version offers:
- No installation required
- Cross-platform compatibility
- Simpler, minimalist design

----------------------------------------
FUTURE IMPROVEMENTS
----------------------------------------
- Add sound effects
- Implement different difficulty levels
- Add parallax scrolling background
- Create mobile touch controls
- Add animation frames for the bird in JavaScript version

----------------------------------------
LICENSE
----------------------------------------
This project is licensed under the MIT License.

----------------------------------------
ACKNOWLEDGMENTS
----------------------------------------
- Original Flappy Bird game created by Dong Nguyen
- Pygame and Phaser.js communities for their excellent documentation

----------------------------------------
This project was created for educational purposes and is not affiliated with 
the original Flappy Bird game.
