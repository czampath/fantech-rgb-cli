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
- To be updated

## Compile Code

   This command will create a single executable file named "fantech.exe" in the "dist" directory within your project folder. The "--onefile" option bundles everything into a single file, "--noconsole" hides the console window, and "--add-data" includes the "data.json" file alongside the executable.

```
pyinstaller --onefile --noconsole --add-data "data.json;." fantech.py
```