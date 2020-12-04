import os

class LocalUpdater:
    def __init__(self):
        pass

    def update(self, filename, newest, shouldUpdate):
        with open("/Users/philipgurr/Documents/Code/Projects/Python/newsletterbot/" + filename + ".txt", "r+") as f:
            lines = f.readlines()
            if len(lines) == 0:
                lines.append("0")
            newest_file = lines[0]
            if shouldUpdate(newest_file, newest):
                f.seek(0)
                f.write(str(newest))
                f.truncate()
                os.system("""osascript -e 'display notification "New {} post is out!"'""".format(filename))