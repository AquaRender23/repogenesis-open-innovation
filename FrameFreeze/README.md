# Frame Freeze

Frame Freeze is a gesture-controlled game platform utilizing MediaPipe Hands and TensorFlow.js for real-time hand gesture recognition. The project includes various interactive mini-games like Car Racing, Table Tennis, Rock-Paper-Scissors, Sudoku, and more, controlled through hand gestures captured via webcam.

## Features

- Hand gesture detection using MediaPipe Hands and TensorFlow.js.
- Multiple gesture-controlled games including:
    - Car racing with swipe and finger gestures.
    - Table tennis game with hand motion control.
    - Rock-Paper-Scissors with hand gesture recognition.
    - Sudoku controlled using hand gestures.
    - Color switch and other mini-games.
- Real-time webcam video capturing and gesture analysis.
- Motion sensor enabled games with keyboard fallback controls.
- Responsive and visually appealing UI with neon-style themes.
- Privacy-focused: no video or data is stored, all processing is local.


## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd FrameFreeze
```

2. Install dependencies (requires Python 3 and Flask):

```bash
pip install -r requirements.txt
```

3. Start the Flask server:

```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000` to start playing.

## Usage

- Allow camera access when prompted to enable gesture recognition.
- Follow on-screen instructions for specific games and gestures.
- Use hand gestures such as swipe left/right, fist, open palm, and peace sign to control gameplay.
- Keyboard controls are available as a fallback for all games.


## Gesture Controls

- Swipe left/right: Change lanes or move objects.
- Fist: Jump or select.
- Open palm: Restart game or pause/unpause.
- Peace sign: Pause or resume gameplay.


## Browser Compatibility

- Compatible with modern browsers: Chrome, Edge, Firefox, Safari.
- Works best with high-quality webcams and good lighting conditions.
- Supports both desktop and tablets with camera.


## Contributing

Contributions are welcome! Please open issues or pull requests for new games, features, or improvements.