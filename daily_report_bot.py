
# ==========================================
# DAILY STATUS REPORT BOT
# Using PyAutoGUI, Chrome and Apple Numbers
# ==========================================

import pyautogui
import pyperclip
import time
import os

from datetime import datetime


# Step 1: Configuration

CITY = "Mumbai"

WEATHER_URL = f"https://wttr.in/{CITY}?format=3"

COMMENT = "Check weather before planning outdoor activities."

# Save reports on Desktop
DESKTOP_PATH = os.path.expanduser("~/Desktop")


# Step 2: Configure PyAutoGUI

# Move mouse to top-left corner to stop automation
pyautogui.FAILSAFE = True

# Wait one second after every PyAutoGUI action
pyautogui.PAUSE = 1


# Step 3: Generate current date and time

now = datetime.now()

current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

current_date = now.strftime("%Y-%m-%d")

numbers_filename = f"daily_report_{current_date}.xlsx"

screenshot_filename = f"daily_report_{current_date}.png"


# Step 4: Function to open an application using Spotlight

def open_application(app_name):

    # Open Mac Spotlight search
    pyautogui.hotkey("command", "space")

    time.sleep(1)

    # Type application name
    pyautogui.write(app_name, interval=0.05)

    time.sleep(2)

    # Press Enter to open application
    pyautogui.press("enter")

    # Wait for application to launch
    time.sleep(5)


# Step 5: Open Chrome and copy weather information

def get_weather():

    print("Opening Google Chrome...")

    open_application("Google Chrome")

    # Focus browser address bar
    pyautogui.hotkey("command", "l")

    # Type weather website URL
    pyautogui.write(WEATHER_URL, interval=0.03)

    # Open website
    pyautogui.press("enter")

    # Wait for website to load
    time.sleep(6)

    # Select all page content
    pyautogui.hotkey("command", "a")

    # Copy selected content
    pyautogui.hotkey("command", "c")

    time.sleep(1)

    # Read copied clipboard content
    weather = pyperclip.paste().strip()

    # Validate copied information
    if not weather:
        raise Exception("Unable to copy weather information!")

    print("Weather information copied successfully!")

    print("Weather:", weather)

    return weather


# Step 6: Open Apple Numbers and create a new spreadsheet

def open_numbers():

    print("\nOpening Apple Numbers...")

    open_application("Numbers")

    # Create a new spreadsheet
    pyautogui.hotkey("command", "n")

    time.sleep(3)

    # Select Blank template if template chooser appears
    pyautogui.press("enter")

    time.sleep(3)

    print("New Numbers spreadsheet created!")


# Step 7: Enter report information into Numbers

def enter_report(weather):

    # Prepare report data using tab-separated values
    report_data = (
        "Date & Time\tWeather Information\tComment\n"
        f"{current_datetime}\t{weather}\t{COMMENT}"
    )

    # Copy report data to clipboard
    pyperclip.copy(report_data)

    # Paste data into Numbers
    pyautogui.hotkey("command", "v")

    time.sleep(2)

    print("Report data entered successfully!")


# Step 8: Save Numbers spreadsheet

def save_numbers():

    print("\nSaving Numbers report...")

    # Open Save dialog
    pyautogui.hotkey("command", "s")

    time.sleep(3)

    # Open Go to Folder
    pyautogui.hotkey("command", "shift", "g")

    time.sleep(1)

    # Enter Desktop folder path
    pyperclip.copy(DESKTOP_PATH)

    pyautogui.hotkey("command", "v")

    pyautogui.press("enter")

    time.sleep(2)

    # Enter Numbers filename
    pyautogui.write(numbers_filename, interval=0.03)

    # Save spreadsheet
    pyautogui.press("enter")

    time.sleep(4)

    print("Numbers report saved:", numbers_filename)


# Step 9: Take screenshot of Numbers

def take_screenshot():

    print("\nTaking Numbers screenshot...")

    time.sleep(2)

    screenshot_path = os.path.join(
        DESKTOP_PATH,
        screenshot_filename
    )

    # Capture current screen
    screenshot = pyautogui.screenshot()

    # Save screenshot
    screenshot.save(screenshot_path)

    print("Screenshot saved:", screenshot_path)


# Step 10: Main program

try:

    print("===== DAILY REPORT BOT STARTED =====")

    # Get weather information
    weather = get_weather()

    # Open Numbers
    open_numbers()

    # Enter report information
    enter_report(weather)

    # Save Numbers file
    save_numbers()

    # Take screenshot
    take_screenshot()

    print("\n===== REPORT COMPLETED SUCCESSFULLY =====")


except Exception as error:

    print("\nAutomation failed:", error)


print("\nDaily Report Bot execution finished!")
