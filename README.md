# Rollwala Attendance Visualizer Bot

This project is a Telegram bot designed to allow users to directly interact with a pre-existing attendance system project, which provides users with visual representations of their attendance data.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)


## Features

- **Telegram Bot Interface**: Enables direct interaction with the attendance system via Telegram.
- **User-Friendly Interaction**: Provides commands and buttons for user engagement.
- **Data Visualization**: Generates and sends visual plots of attendance data directly to the user.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/attendance-visualizer-bot.git
    cd attendance-visualizer-bot
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Telegram Bot**:

   - Obtain a bot token by creating a bot using [BotFather](https://t.me/BotFather) on Telegram.
   - Update the `TELEGRAM_BOT_TOKEN` in `config.py` with your bot token.

4. **Run the bot**:

    ```bash
    python bot.py
    ```

## Usage

- Start the bot by sending the `/start` command.
- Follow the instructions to enter your email and password.
- Choose your track and wait for your attendance visualization.

## File Structure

- **bot.py**: Main script to start the bot.
- **config.py**: Configuration file containing URLs and bot token.
- **handlers.py**: Handles various bot commands and user interactions.
- **services.py**: Contains functions to fetch data from the backend system.
- **plots.py**: Generates visual plots of the attendance data.
- **utils.py**: Utility functions for data processing.

## Acknowledgements

- **Core Attendance System**: The backend code for the attendance system was originally developed by @git-biswojit Special thanks to him for their hard work on the data processing scripts.

## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.
