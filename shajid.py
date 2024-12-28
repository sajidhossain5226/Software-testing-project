from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with webdriver.Firefox() if using Firefox
driver.maximize_window()

try:
    # Open the Restful Booker platform demo site
    driver.get("https://automationintesting.online/")
    print("Opened the website successfully.")

    # Wait for the "single" room section to load
    wait = WebDriverWait(driver, 20)
    single_room_header = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'single')]"))
    )
    print("Single room section located.")

    # Scroll to the "Book now" button
    book_now_button = single_room_header.find_element(
        By.XPATH, "./following-sibling::div//button[contains(text(), 'Book now')]"
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", book_now_button)
    print("Scrolled to the 'Book now' button.")

    # Click the "Book now" button
    book_now_button.click()
    print("Clicked the 'Book now' button.")

    # Fill out the booking form
    first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.room-firstname")))
    first_name.send_keys("John")
    print("Entered first name.")

    last_name = driver.find_element(By.CSS_SELECTOR, "input.room-lastname")
    last_name.send_keys("Doe")
    print("Entered last name.")

    email = driver.find_element(By.CSS_SELECTOR, "input.room-email")
    email.send_keys("johndoe@example.com")
    print("Entered email.")

    phone = driver.find_element(By.CSS_SELECTOR, "input.room-phone")
    phone.send_keys("1234567890")
    print("Entered phone number.")

    # Submit the booking form
    book_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Book')]")
    book_button.click()
    print("Clicked the 'Book' button.")

    # Wait for the confirmation message
    confirmation_message = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Booking successful') or contains(text(),'Thank you')]"))
    )
    print("Booking successfully completed!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    time.sleep(2)
    driver.quit()
