# ==========================================
# CAPTURE A LIVE CRICKET SCORE WITH PLAYWRIGHT
# ==========================================

# Import Playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Start Playwright
with sync_playwright() as p:
    # Launch Chromium browser
    # headless=False means browser is visible
    browser = p.chromium.launch(headless=False)

    try:
        # Create a new browser page
        page = browser.new_page()

        # Open Cricbuzz
        page.goto("https://www.cricbuzz.com/", wait_until="domcontentloaded")

        print("Cricbuzz website opened successfully!")

        # Find the score element
        score_element = page.locator('a.w-\\[300px\\][href*="/live-cricket-scores/161285/"]')

        # Wait until score element becomes visible
        score_element.wait_for(
            state="visible",
            timeout=15000
        )

        # Extract score text
        score = score_element.inner_text().strip()

        # Print score in terminal
        print("\nLIVE CRICKET SCORE")
        print("-" * 40)
        print(score)
        print("-" * 40)

        # Take screenshot
        page.screenshot(path="score.png")

        print("\nScreenshot saved as score.png")

    except PlaywrightTimeoutError:

        # Handle situation when score is not available
        print("No live score found within the waiting time.")
        print("There may be no live match or the selector may be incorrect.")

        # Save screenshot for debugging
        page.screenshot(path="score.png")

        print("Debug screenshot saved as score.png")

    except Exception as error:

        # Handle unexpected errors
        print("Something went wrong:", error)

    finally:

        # Step 11: Close browser
        browser.close()

        print("\nBrowser closed successfully!")