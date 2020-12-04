from scrapers import *
from updater import LocalUpdater

kotlin_scraper = KotlinScraper()
newest_kotlin = kotlin_scraper.get_newest()
print("Kotlin: " + newest_kotlin)

android_scraper = AndroidScraper()
newest_android = android_scraper.get_newest()
print("Android: " + str(newest_android))

updater = LocalUpdater()
updater.update_kotlin(newest_kotlin)
updater.update_android(newest_android)