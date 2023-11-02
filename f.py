#pip install selenium-driverless
#pip install selenium_profiles

from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium_driverless.webdriver import ChromeOptions
from selenium_driverless.types.by import By
from selenium_driverless.types.webelement import NoSuchElementException
import time

profile = profiles.Windows() # or .Android
options = ChromeOptions()
driver = Chrome(profile=profile, options=options, driverless_options=True)

back = driver.current_window_handle
# get url
driver.get('https://www.bet365.com/#/IP/B151')
#driver.switch_to.target(driver.targets[0]["targetId"])

time.sleep(20)

driver.switch_to.target(back)
#f = driver.find_element(By.CSS_SELECTOR, "div.ovm-MarketGroupEsports.span.ovm-ParticipantOddsOnly_Odds").text
#fx = driver.find_element(By.XPATH, "//div[text()='Esoccer Battle - 8 mins play']")
fx = driver.find_element(By.XPATH, "//div[text()='Esoccer GT Leagues - 12 mins play']")
fxp = fx.find_element(By.XPATH, "../../../..")
ffd = fxp.find_elements(By.CSS_SELECTOR, "div.ovm-Fixture_Container")
for ffdx in ffd:
	ffdxf = ffdx.find_elements(By.CSS_SELECTOR, "div.ovm-FixtureDetailsTwoWay_TeamName")
	for ffdxff in ffdxf:
		print(ffdxff.text)
	fro = ffdx.find_elements(By.CSS_SELECTOR, "span.ovm-ParticipantOddsOnly_Odds")
	for f in fro:
		print(f.text)
	print()
	print()

driver.quit()  #