import json

class Animation:
    def __init__(self, script):
        self.shouldRun = True
        self.script = script
        self.chords = json.load(open("L://Dev/xmaslights-v2/chords.json"))

    def stop(self):
        self.shouldRun = False
