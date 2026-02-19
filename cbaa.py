import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
from dotenv import load_dotenv
from utils.parse_feature import parse_and_hydrate_gherkin
import threading
import json

load_dotenv()
USER_NAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

options = ChromeOptions()
options.set_capability('browserName', 'Chrome')
bstack_options = {
    "os": "Windows",
    "osVersion": "10",
    "projectName": "BrowserStack AI Authoring",
    "buildName": "AI-Python-Demo",
    "sessionName": "Ecommerce Test Flow",
    "userName": USER_NAME,
    "accessKey": ACCESS_KEY,
    "aiAuthoring": "true"
}
options.set_capability('bstack:options', bstack_options)


def ai_execute(command, driver):
    """Helper function to run AI natural language commands"""

    print(f"Executing AI Command: {command}")
    params = {
        "action": "ai",
        "arguments": [command]
    }

    json_string = json.dumps(params)
    driver.execute_script(f'browserstack_executor: {json_string}')

def run_test_session(name, steps, options):
    """Function logic to be executed by each thread."""
    print(f"🚀 Thread starting: Executing {len(steps)} steps...\n")
    
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    executor_object = {
        "action": "setSessionName",
        "arguments": {
            "name": name
        }
    }


    driver.execute_script(f'browserstack_executor: {json.dumps(executor_object)}')
    
    try:
        driver.get("https://ecommercebs.vercel.app/")
        time.sleep(2)
        driver.maximize_window()

        for index, command in enumerate(steps, start=1):
            print(f"Step {index}: {command}")
            ai_execute(command, driver) 

        print("\n✅ Purchase scenario flow completed successfully using AI Authoring")
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Purchase scenario flow completed successfully using AI Authoring."}}')
    
    except Exception as e:
        print(f"❌ Error in thread: {e}")
        reason_str = json.dumps(str(e))[1:-1] 

        driver.execute_script(
            f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "{reason_str}"}}}}'
        )
    
    finally:
        driver.quit()

try:
    relative_file_path = "../features/purchase.feature"
    final_arrays = parse_and_hydrate_gherkin(relative_file_path)

    threads = []
    for i, commands in enumerate(final_arrays):
        print(f"Creating thread {i}")
        thread = threading.Thread(target=run_test_session, args=(commands['name'], commands['steps'], options))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

except Exception as e:
    print(f"Error encountered: {e}")