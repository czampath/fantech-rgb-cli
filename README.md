# Fantech RGB Keyboard CLI Control

## Overview
Fantech RGB CLI, built upon reverse engineering techniques, simplifies RGB lighting management for Fantech RGB gaming peripherals (keyboard/mouse). Easily control, automate and switch between a variety of lighting effects using command-line interface. It was initially developed for personal use and later made available to the public.

## Compatibility
Fantech RGB Keyboard CLI Control is specifically designed for use with **FANTECH OPTILUXS MK884 RGB GAMING KEYBOARD.** It may not be compatible with other keyboard models.

## Features
- Control RGB lighting effects of the Fantech RGB gaming keyboard.
- Simple command-line interface for ease of use.
- Compatible with Windows operating systems.

## Requirements
- Fantech RGB gaming keyboard (specifically, the model OPTILUXS MK884)
- Windows operating system
- Knowledge of basic command-line interface (CLI) usage

## Usage
1. Download the packaged executable from the release section of the GitHub repository.
2. Connect the Fantech RGB gaming keyboard to your computer via USB.
3. Open the command prompt (CMD) in the directory where the executable is located.
4. Run the executable with appropriate command-line arguments to send setup packets to the keyboard.
5. Verify the desired changes or effects on the keyboard's behavior.
6. Customize the command-line arguments as needed for different lighting effects.

## Command-line Arguments

- `--set-style [style]` (Required):
  - Specify the desired RGB effect style.
  - The style must be one of the supported effects.
  - Example: `--set-style shuttle`
  
- `--color [color]` (Optional):
  - Specify the color for the chosen effect.
  - If no color is provided, the default color for the effect will be used.
  - Example: `--set-style shuttle --color red`

- `--get-style [style]`:
  - Use `*` to list all unique styles without colors.
  - Example: `python fantech.py --get-style *` will return:
    ```
    default
    off
    rotating
    spectrum
    shuttle
    ```
  - Pass a specific style to list all available colors for that style.
  - Example: `python fantech.py --get-style shuttle` will return:
    ```
    default
    red
    ```

- `--help`:
  - Displays the help message with descriptions of all available command-line arguments.
  - Example: `python fantech.py --help`

### Example Commands:

- Set an RGB effect with default color:
  ```bash
  python fantech.py --set-style shuttle
  ```
- Set an RGB effect with a specific color:
  ```bash
  python fantech.py --set-style static --color red
  ```
- List all styles:
  ```bash
  python fantech.py --get-style *
  ```
- List all colors for a specific style:
  ```bash
  python fantech.py --get-style shuttle
  ```
In case the device cannot be found, the tool will attempt auto-configuration based on the default `vendor_id` and `product_id`.

## Compile Code

   This command will create a single executable file named "fantech.exe" in the "dist" directory within your project folder. The "--onefile" option bundles everything into a single file, "--noconsole" hides the console window, and "--add-data" includes the "data.json" file alongside the executable.

```
pyinstaller --onefile --noconsole --add-data "data.json;." fantech.py
```