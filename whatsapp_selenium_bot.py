from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def open_whatsapp_web():
    """
    Opens WhatsApp Web and keeps the browser open for operations.
    Returns the WebDriver instance.
    """
    # Path to ChromeDriver in your project folder
    driver_path = "f:/MINECRAFT FILES/Python Projects/Bots/Egy Edu Bot/egy-edu-bot/chromedriver/chromedriver.exe"
    
    # Set up Chrome options to use a persistent user data directory
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=f:/MINECRAFT FILES/Python Projects/Bots/Egy Edu Bot/chrome-data")  # Path to store session data

    # Initialize the WebDriver with the Chrome options
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("If not already logged in, scan the QR code to log in to WhatsApp Web.")

    # Wait until the user logs in by checking for the presence of the search box
    while True:
        try:
            driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            print("Logged in successfully!")
            break
        except:
            time.sleep(1)  # Keep checking every second

    return driver

def send_message(driver, phone_number, message):
    """
    Sends a WhatsApp message to the specified phone number.
    """
    try:
        # Search for the contact or phone number
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()
        search_box.send_keys(phone_number)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

        # Type and send the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print(f"Message sent successfully to {phone_number}!")
    except Exception as e:
        print(f"Failed to send message to {phone_number}. Error: {e}")

def main():
    """
    Main function to open WhatsApp Web and perform operations dynamically.
    """
    driver = open_whatsapp_web()

    """
    while True:
        # Get inputs from the user
        phone_number = input("Enter the recipient's phone number (in international format, e.g., +1234567890): ").strip()
        message = input("Enter the message to send: ").strip()

        # Send the message
        send_message(driver, phone_number, message)

        # Ask if the user wants to send another message
        another = input("Do you want to send another message? (yes/no): ").strip().lower()
        if another != "yes":
            print("Exiting...")
            break
    """
    print("Browser will remain open. Close it manually when done.")
    stay_alive(driver)

def stay_alive(driver):
    """
    Keeps the browser alive indefinitely.
    """
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        print("Exiting and closing the browser...")
        driver.quit()

# Example usage
if __name__ == "__main__":
    main()