import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from webdriver_manager.chrome import ChromeDriverManager


class NyscBot:
	def __init__(self) -> None:
		self.option = Options()
		self.option.add_argument("--headless")
		self.slackClient = WebClient(token="xoxb-3056601028273-3044089109794-FmNzmZupQw3tXaKRQhHepiuy")
		self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.option)
	
	def open_url(self,url:str)-> None:
		self.driver.get(url)
	
	def save_screenshot(self,file_path:str)-> None:
		image = Path(file_path)
		if image.is_file():
			os.remove(file_path)
		self.driver.save_screenshot(file_path)


	def send_image(self,image_path:str)-> None:
		try:
			self.slackClient.files_upload(channels="bot", file=image_path)
		except SlackApiError as e:
			print("Error uploading file: {}".format(e))

def main():
	bot = NyscBot()
	bot.open_url('https://portal.nysc.org.ng/nysc1/')
	bot.save_screenshot('screenshot.png')
	bot.send_image('screenshot.png')
	bot.save_screenshot('screenshot.png')


if __name__ == '__main__':
	main()







