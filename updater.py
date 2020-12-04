import os

class LocalUpdater:
    def __init__(self):
        pass

    def update_android(self, newest_android):
        with open("/Users/philipgurr/Documents/Code/Projects/Python/newsletterbot/android.txt", "r+") as f:
            newest_file = f.readlines()[0]
            if not newest_file:
                newest_file = 0
            if newest_android > int(newest_file):
                f.seek(0)
                f.write(str(newest_android))
                f.truncate()
                os.system("""osascript -e 'display notification "New {} is out!"'""".format(android_scraper.prefix + str(newest_android)))

    def update_kotlin(self, newest_kotlin):
        with open("/Users/philipgurr/Documents/Code/Projects/Python/newsletterbot/kotlin.txt", "r+") as f:
            lines = f.readlines()
            if len(lines) == 0:
                lines.append("")
            newest_file = lines[0]
            if newest_kotlin != newest_file:
                f.seek(0)
                f.write(str(newest_kotlin))
                f.truncate()
                os.system("""osascript -e 'display notification "New Kotlin Blog Post available!"'""")