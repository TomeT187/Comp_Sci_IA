class presets():
    def __init__(self):
        self.presetArray = []
        self.readPresets()

    def addPreset(self,newPreset):
        self.presetArray.append(newPreset)
        self.writePresets()

    def readPresets(self):
        presetFile = open("presets.txt","r")
        line = presetFile.read()
        self.presetArray = line.split(",")
        self.presetArray.pop(len(self.presetArray ) - 1)
        #reads from file

    def writePresets(self):
        presetFile = open("presets.txt","w")
        for i in self.presetArray:
            presetFile.write(i + ",")