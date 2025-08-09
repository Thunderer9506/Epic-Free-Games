# Epic Free Games Notifier

This Python project scrapes the Epic Games Store for currently available free games and sends a WhatsApp notification with the details using `pywhatkit`.

## Features

- Uses Selenium to scrape the Epic Games Store free games page.
- Extracts game status, name, and time left for the next free game.
- Sends a WhatsApp message with the details to a specified phone number.
- Logs sent messages in `PyWhatKit_DB.txt`.

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- [Selenium](https://pypi.org/project/selenium/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)

## Installation

1. Clone this repository or download the files.
2. Install the required Python packages:
    ```sh
    pip install selenium pywhatkit
    ```
3. Download and place the correct version of ChromeDriver in your PATH.

## Usage

1. Edit `main.py` and replace the phone number in the `pywhatkit.sendwhatmsg` call with your own.
2. Run the script:
    ```sh
    python main.py
    ```
3. The script will open WhatsApp Web in your browser and send the message at the scheduled time.

## Files

- [`main.py`](main.py): Main script for scraping and sending messages.
- [`PyWhatKit_DB.txt`](PyWhatKit_DB.txt): Log of sent messages.

## Notes

- Make sure you are logged into WhatsApp Web in your browser before running the script.
- The script schedules the message to be sent one minute after execution.
