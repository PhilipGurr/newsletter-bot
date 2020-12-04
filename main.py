from scrapers import *
from updater import LocalUpdater

kotlin_scraper = KotlinScraper()
newest_kotlin = kotlin_scraper.get_newest()
print("Kotlin: " + newest_kotlin)

android_scraper = AndroidScraper()
newest_android = android_scraper.get_newest()
print("Android: " + str(newest_android))

updater = LocalUpdater()
updater.update("kotlin", newest_kotlin, lambda old, new: new != old)
updater.update("android", newest_android, lambda old, new: new > int(old))