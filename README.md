# Flappy Bird Clone
A Python implementation of the classic Flappy Bird game using Pygame.
DESCRIPTION
This project is a faithful recreation of the popular mobile game Flappy Bird.
Navigate a bird through a series of pipes by tapping the spacebar to flap the
bird's wings. The game features smooth animations, particle effects, and keeps
track of your high score.
FEATURES
- Custom-drawn bird sprite with wing flapping animation
Physics-based movement with gravity and momentum
Randomly generated pipes with varying gap positions
Score tracking and high score system
Animated clouds and environmental details
Game over screen with restart option
Attractive title screen
CONTROLS
SPACE: Flap wings / Start game / Restart after game over
REQUIREMENTS
- Python 3.6+
Pygame 2.0+



INSTALLATION
1. Clone the repository:
git clone https://github.com/yourusername/flappy-bird-clone.git
cd flappy-bird-clone
Install the required dependencies:
pip install pygame
Run the game:
python yuh.py
CODE STRUCTURE
- create_bird_sprite(): Generates the bird sprite with custom drawing
Bird class: Handles bird physics, animation, and collision detection
Pipe class: Manages pipe generation, movement, and rendering
Game class: Controls game state, scoring, and user interface
CUSTOMIZATION
You can modify the following constants at the top of the file to adjust gameplay:
GRAVITY: Controls how quickly the bird falls
FLAP_STRENGTH: Determines how high the bird jumps when flapping
PIPE_SPEED: Sets how fast pipes move across the screen
PIPE_SPAWN_RATE: Controls the time between pipe spawns
PIPE_GAP: Adjusts the size of the gap between pipes
LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.
ACKNOWLEDGMENTS
- Original Flappy Bird game created by Dong Nguyen
Pygame community for their excellent documentation and examples
FUTURE IMPROVEMENTS
- Add sound effects
Implement different difficulty levels
Add parallax scrolling background
Create mobile touch controls
Add animation frames for the bird
This project was created for educational purposes and is not affiliated with the
original Flappy Bird game.
