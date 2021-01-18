import logging
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils


class VarColsPerWaveFactory():
    varsColsPerWaveMapping = {}

    def __init__(self):
        self.varsColsPerWaveMapping = CreateDataSetUtils.loadVarsColsPerWaveMapping()

    def getEmpty(self):
        return {"cols_empty": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
        },
            "reversed_cols_empty": {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
        }}

    def getAllVarsMapping(self):
        return self.varsColsPerWaveMapping

    def getColsForWaves(self, varName):
        return self.varsColsPerWaveMapping[varName]
