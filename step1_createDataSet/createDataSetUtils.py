from os import PathLike
import pathlib
from numpy.core.numeric import NaN
import pandas as pd
import logging
import json


class CreateDataSetUtils:
    rawDataFolder = ''
    outputDataFolder = ''
    indexColName = ''

    @staticmethod
    def getIndexColName():
        return CreateDataSetUtils.indexColName

    @staticmethod
    def getRawDataFolder():
        return CreateDataSetUtils.rawDataFolder

    @staticmethod
    def getOutputDataFolder():
        return CreateDataSetUtils.outputDataFolder

    @staticmethod
    def loadRawDataIntoDf(rawDataFileLocation):
        return pd.read_csv(rawDataFileLocation)

    @staticmethod
    def loadWaveData(waveNumber):
        path = CreateDataSetUtils.getRawDataFolder() + 'wave' + \
            str(waveNumber) + '.csv'
        logging.debug('Loading wave data from ' + path)
        df = CreateDataSetUtils.loadRawDataIntoDf(path)
        if not (CreateDataSetUtils.verifyIndex(df, CreateDataSetUtils.indexColName)):
            raise Exception(
                "Wave " + waveNumber + " doesnt follow index on it's col: " + CreateDataSetUtils.indexColName)
        return df

    @staticmethod
    def loadCurrentVarsMeansData():
        path = CreateDataSetUtils.getOutputDataFolder(
        ) + '\\MeansOfMainVarsAcrossAllWaves.csv'
        logging.debug('Loading vars means data from ' + path)
        return CreateDataSetUtils.loadRawDataIntoDf(path)

    @ staticmethod
    def loadVarsColsPerWaveMapping():
        path = CreateDataSetUtils.getRawDataFolder() + \
            '\\varsColsPerWaveMapping.json'
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def createIndexFile(indexColName, sourceFile):
        w1Df = CreateDataSetUtils.loadRawDataIntoDf(sourceFile)
        w1Df[indexColName].to_csv(
            CreateDataSetUtils.rawDataFolder+'\\index.csv')

    @staticmethod
    def getIndex():
        indexDf = CreateDataSetUtils.loadRawDataIntoDf(
            CreateDataSetUtils.rawDataFolder+'\\index.csv')
        return indexDf[CreateDataSetUtils.indexColName]

    @staticmethod
    def verifyIndex(df, indexColOnSentDf):
        return CreateDataSetUtils.getIndex().equals(df[indexColOnSentDf])

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
