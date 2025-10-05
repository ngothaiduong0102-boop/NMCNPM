import os, time, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def build_url(args):
    if args.local:
        p = os.path.abspath(args.local)
        if not os.path.exists(p): raise SystemExit(f"File not found: {p}")
        return f"file://{p}"
    base = os.getenv("BASE_URL", "").strip()
    if not base: raise SystemExit("Set BASE_URL or use --local /path/to/index.html")
    return base

def run_case(driver, username, password, expect):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys(username or "")
    driver.find_element(By.ID, "password").send_keys(password or "")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(0.5)
    alert = driver.switch_to.alert
    msg = alert.text
    assert expect in msg
    alert.accept()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local", help="Path to Lab04 index.html")
    ap.add_argument("--screenshot-dir", default="screenshots")
    args = ap.parse_args()

    url = build_url(args)
    os.makedirs(args.screenshot_dir, exist_ok=True)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1024, 768)
    try:
        driver.get(url)
        run_case(driver, "", "", "Vui lòng nhập")
        driver.save_screenshot(os.path.join(args.screenshot_dir, "empty.png"))
        run_case(driver, "demo", "123", "ít nhất 6")
        driver.save_screenshot(os.path.join(args.screenshot_dir, "short.png"))
        run_case(driver, "demo", "123456", "Đăng nhập thành công")
        driver.save_screenshot(os.path.join(args.screenshot_dir, "success.png"))
        print("[OK] Selenium tests passed.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
