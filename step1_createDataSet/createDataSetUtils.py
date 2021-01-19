from numpy.core.numeric import NaN
import pandas as pd
import logging
import json


class CreateDataSetUtils:
    rawDataFolder = ''
    indexColName = ''

    @staticmethod
    def getIndexColName():
        return CreateDataSetUtils.indexColName

    @staticmethod
    def getRawDataFolder():
        return CreateDataSetUtils.rawDataFolder

    @staticmethod
    def loadRawDataIntoDf(rawDataFileLocation):
        return pd.read_csv(rawDataFileLocation)

    @staticmethod
    def loadWaveData(waveNumber):
        path = CreateDataSetUtils.getRawDataFolder() + '\\wave' + \
            str(waveNumber) + '.csv'
        logging.debug('Loading wave data from ' + path)
        return CreateDataSetUtils.loadRawDataIntoDf(path)

    @ staticmethod
    def loadVarsColsPerWaveMapping():
        path = CreateDataSetUtils.getRawDataFolder() + \
            '\\varsColsPerWaveMapping.json'
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    @ staticmethod
    def reverseLikhert(ans):
        if ans.strip() == '':
            return NaN
        ansInt = int(ans)
        switcher = {
            1: 7,
            2: 6,
            3: 5,
            4: 4,
            5: 3,
            6: 2,
            7: 1,
        }
        return switcher.get(ansInt, NaN)
