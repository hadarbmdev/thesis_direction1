import pandas as pd
import logging
import pathlib


class CreateDataSetUtils:
    @staticmethod
    def loadRawDataIntoDf(rawDataFileLocation):
        logging.debug(
            'loading raw data from ' + rawDataFileLocation)
        return pd.read_csv(rawDataFileLocation)

    @staticmethod
    def loadWaveData(waveNumber):
        return CreateDataSetUtils.loadRawDataIntoDf(str(pathlib.Path().absolute()) + '\\step1_createDataSet\\rawData\\wave' + str(waveNumber) + '.csv')

    @staticmethod
    def reverseLikhert(ans):
        switcher = {
            1: 7,
            2: 6,
            3: 3,
            4: 4,
            5: 5,
            6: 2,
            7: 1,
        }
        return switcher.get(ans, -1)
