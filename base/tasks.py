# myapp/tasks.py
from celery import shared_task
from DrissionPage import ChromiumPage, ChromiumOptions
import pyperclip

@shared_task
def process_user_input(text):
    co = ChromiumOptions()
    co.headless(False)
    driver = ChromiumPage(co)
    driver.get("https://chatgpt.com/")
    textarea = driver.ele("#prompt-textarea")
    textarea.clear()
    textarea.input(text)
    driver.ele('xpath://*[@id="__next"]/div/div/main/div[1]/div[2]/div[1]/div/form/div/div[2]/div/div/button').click()
    driver.wait.ele_displayed('xpath://*[@id="__next"]/div/div[2]/main/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/span[2]/button')
    driver.ele('xpath://*[@id="__next"]/div/div[2]/main/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/span[2]/button').click()
    driver.ele('xpath://*[@id="__next"]/div/div[2]/main/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/span[2]/button').click()
    
    driver.quit()
    pasted_text = pyperclip.paste()
    return pasted_text
