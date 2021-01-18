import pandas as pd
import logging
import pathlib
import json


class CreateDataSetUtils:
    @staticmethod
    def loadRawDataIntoDf(rawDataFileLocation):
        logging.debug(
            'loading raw data from ' + rawDataFileLocation)
        return pd.read_csv(rawDataFileLocation)

    @staticmethod
    def loadWaveData(waveNumber):
        path = str(pathlib.Path().absolute()) + '\\step1_createDataSet\\rawData\\wave' + \
            str(waveNumber) + '.csv'
        logging.debug('Loading wave data from ' + path)
        return CreateDataSetUtils.loadRawDataIntoDf(path)

    @ staticmethod
    def loadVarsColsPerWaveMapping():
        path = str(pathlib.Path().absolute()) + \
            '\\step1_createDataSet\\rawData\\varsColsPerWaveMapping.json'
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    @ staticmethod
    def reverseLikhert(ans):
        switcher = {
            1: 7,
            2: 6,
            3: 5,
            4: 4,
            5: 3,
            6: 2,
            7: 1,
        }
        return switcher.get(ans, -1)
