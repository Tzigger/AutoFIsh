# Fishing Automation Script for FIVEM

This script automates the fishing job in the game FIVEM using bit processing. It constantly checks the color of a specific pixel on the screen and performs certain actions when the color matches the target color.

## Prerequisites

- Python 3.x
- The `keyboard` and `PIL` libraries for Python. You can install them using pip:
  
```
  pip install keyboard pillow
```
## How it Works

The script uses the `ImageGrab` module from the `PIL` library to capture a screenshot of a 1x1 pixel region of the screen. It then converts the image to RGB format and retrieves the RGB value of the top-left pixel.

The script then checks if the RGB value of the pixel matches the target color. If it does, it simulates the key press and release of the `e` key, which performs the fishing action in the game.

Additionally, the script checks the color of a second pixel to verify if the fishing action was successful. If the color of the second pixel matches either of the two expected colors, the script simulates the key press and release of the `e` key to continue fishing.

## Setup

1. Open the script in a text editor.
2. Modify the `target_color` variable to match the RGB value of the pixel you want to track in the game.
3. Save the script and run it using Python.

## Usage

Once the script is running, it will constantly check the color of the specified pixel and perform the fishing action when the color matches the target color.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
