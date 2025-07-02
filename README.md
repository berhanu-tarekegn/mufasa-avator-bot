# Awesome Avatar Generator Bot

This is a Telegram bot that generates cool looking avatars based on the name you enter. It uses the service from `http://avatars.adorable.io/` to generate avatars.

## Features

- Welcomes users with a greeting message.
- Generates avatars based on user input.
- Sends avatars as photos in the chat.
- Sets up a webhook for Telegram updates.

## Requirements

- Python 3.12 or higher
- FastAPI
- Uvicorn
- python-telegram-bot
- pydantic-settings

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd avatorbot
   ```

2. **Install dependencies:**

   Use Poetry to install the required dependencies:

   ```bash
   poetry install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add the following variables:

   ```env
   TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
   TELEGRAM_BOT_USERNAME=<your-telegram-bot-username>
   BASE_URL=<your-base-url>
   ```

   Replace `<your-telegram-bot-token>`, `<your-telegram-bot-username>`, and `<your-base-url>` with your actual values.

## Usage

1. **Run the application:**

   Use Uvicorn to run the FastAPI application:

   ```bash
   poetry run uvicorn main:app --reload
   ```

2. **Set the webhook:**

   Access the `/setwebhook` endpoint to set up the webhook for Telegram updates:

   ```bash
   http://<your-base-url>/setwebhook
   ```

3. **Interact with the bot:**

   Start a chat with your bot on Telegram and enter a name to receive an avatar.

## Acknowledgments

Special thanks to Ali Abdel Aal

## File Descriptions

- `config.py`: Contains the configuration settings for the application using Pydantic.
- `main.py`: The main application file that handles incoming Telegram messages and generates avatars.
- `pyproject.toml`: Contains the project metadata and dependencies managed by Poetry.
- `.env`: Stores environment variables for sensitive information like the Telegram bot token.

## License

This project is licensed under the MIT License.
