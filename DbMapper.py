class DbMapper():
    def __init__(self, line):
        s = line.split(",")
        self.headerToIndexMap = {}

        i = 0
        for val in s:
            self.headerToIndexMap[val.strip().lower()] = i

            i += 1

    def getValue(self, content, column):
        cells = content.split(",")

        key = column
        if key in self.headerToIndexMap:
            val = cells[self.headerToIndexMap[key]]
            return val
        
        return None