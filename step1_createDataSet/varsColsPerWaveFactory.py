import logging
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils
from step1_createDataSet.varsStrcture.subjectVar import SubjectsVarsEnum


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

    def getColsForWaves(self, varName):
        return self.varsColsPerWaveMapping[varName]
