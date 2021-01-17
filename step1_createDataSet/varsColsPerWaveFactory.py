import logging
import enum
from step1_createDataSet.varsStrcture.subjectVar import SubjectsVarsEnum


class VarColsPerWaveFactory():
    @staticmethod
    def getEmpty():
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

    @staticmethod
    def getColsForWaves(varName):
        switcher = {
            SubjectsVarsEnum.OrganismicFaith.name: {
                "cols": {
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: [],
                    6: [],
                    7: [],
                },
                "reversed_cols": {
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: [],
                    6: [],
                    7: [],
                }
            },
        }
        return switcher.get(varName, VarColsPerWaveFactory.getEmpty())
