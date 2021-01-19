from abc import ABCMeta, abstractmethod
from os import PathLike
import pathlib
from types import resolve_bases

from pandas.core.indexes.base import Index
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils
import pandas
import logging


class SubjectVar():
    __metaclass__ = ABCMeta

    def __init__(self, label, all_cols, indexColName):
        self.label = label
        self.indexColName = indexColName
        self.df = pandas.DataFrame()
        print('[SubjectVar] ' + str(all_cols))
        self.waves = all_cols['waves']
        self.cols = all_cols['cols']
        self.reversed_cols = all_cols['reversed_cols']
        print('[SubjectVar] ' + self.getLabel())
        logging.debug("calculating " + self.getSubjectPrefix() +
                      " - " + self.getLabel())
        self.compute()

    @abstractmethod
    def isMother(self):
        pass

    @abstractmethod
    def isChild(self):
        pass

    @abstractmethod
    def getLabel(self):
        return self.label

    @abstractmethod
    def getIndexColName(self):
        return self.indexColName

    @abstractmethod
    def getSubjectPrefix(self):
        pass

    @property
    @abstractmethod
    def getDataset(self):
        return self.df

    @property
    @abstractmethod
    def getWaves(self):
        return self.waves

    def compute(self):
        self.computeVarAcrossRelevantWaves()

    def computeVarAcrossRelevantWaves(self):
        mainVarPerWave = pandas.DataFrame()
        for waveNumber in self.getWaves:
            waveNumberStr = str(waveNumber)
            meanVarName = self.getLabel() + '_wave' + waveNumberStr
            mainVarDf = self.getDfForThisVarOnWave(waveNumberStr, meanVarName)
            mainVarPerWave[meanVarName] = mainVarDf[meanVarName]
        print(mainVarPerWave)

    # returns a DF that is based only on the relevant columns for this main var
    def getDfForThisVarOnWave(self, waveNumberStr, meanVarName):
        logging.debug('computing wave number '+str(waveNumberStr))
        outputFileName = meanVarName + ".csv"
        outputFilePath = str(pathlib.Path().absolute()) + \
            '\\step1_createDataSet\\output\\'
        waveDf = CreateDataSetUtils.loadWaveData(waveNumberStr)
        waveDf = self.recodeReversedColsInPlace(
            waveDf, self.reversed_cols[str(waveNumberStr)])

        # filter only this var cols to a new fresh data set of this var for this wave
        mainVarDf = waveDf.filter(self.cols[waveNumberStr] +
                                  self.reversed_cols[waveNumberStr], axis=1)

        for column in mainVarDf:
            mainVarDf[column] = pandas.to_numeric(
                mainVarDf[column], errors='coerce')

        mainVarDf.to_csv(outputFilePath + 'base_' +
                         outputFileName, index=False)

        # Add mean column for this var (like SPSS compute across these var sub - variables)
        mainVarDf[meanVarName] = mainVarDf.mean(axis=1, skipna=True)

        # add the index column, after we already calculated mean on all other columns
        mainVarDf.insert(0, self.getIndexColName(),
                         waveDf[self.getIndexColName()])

        mainVarDf.to_csv(outputFilePath + outputFileName, index=False)
        return mainVarDf

    def recodeReversedColsInPlace(self, df, cols):
        if (len(cols) > 0):
            logging.debug("recoding cols " + str(cols))
            for col in cols:
                logging.debug(col+'_R, before: ' + str(df[col+'_R']))
                df[col +
                    '_R'] = df[col].apply(CreateDataSetUtils.reverseLikhert())
                logging.debug(col+'_R, after: ' + str(df[col+'_R']))
                df[col] = df[col+'_R']
                df.drop(col+'_R', axis=1, inplace=True)
                logging.debug(col + ' final : ' + str(df[col+'_R']))
        return df


class MotherVar(SubjectVar):
    __metaclass__ = ABCMeta

    def __init__(self, label, all_cols, indexColName):
        super(MotherVar, self).__init__(label, all_cols, indexColName)

    def isMother(self):
        return True

    def isChild(self):
        return False

    def getSubjectPrefix(self):
        return 'Mother'


class ChildVar(SubjectVar):

    __metaclass__ = ABCMeta

    def __init__(self, label, all_cols, indexColName):
        super(ChildVar, self).__init__(label, all_cols, indexColName)

    def isMother(self):
        return False

    def isChild(self):
        return True

    def getSubjectPrefix(self):
        return 'Child'
