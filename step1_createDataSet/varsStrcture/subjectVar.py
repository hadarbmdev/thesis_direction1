from abc import ABCMeta, abstractmethod
from types import resolve_bases
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils
import pandas
import logging
from enum import Enum


class SubjectsVarsEnum(Enum):
    OrganismicFaith = "Organismic Faith"


class SubjectVar():
    __metaclass__ = ABCMeta

    def __init__(self, label, all_cols):
        self.label = label
        self.df = pandas.DataFrame()
        print(all_cols)
        self.cols = all_cols['cols']
        self.reversed_cols = all_cols['reversed_cols']
        print(self.getLabel())
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
    def getSubjectPrefix(self):
        pass

    @property
    @abstractmethod
    def getDataset(self):
        return self.df

    @property
    @abstractmethod
    def getWaves(self):
        return []

    def compute(self):
        self.computeVarAcrossRelevantWaves()

    def computeVarAcrossRelevantWaves(self):
        for waveNumber in self.getWaves:
            waveDf = CreateDataSetUtils.loadWaveData(waveNumber)
            waveDf = self.recodeReversedColsInPlace(
                waveDf, self.reversed_cols[waveNumber])
            groupBy = self.cols[waveNumber] + self.reversed_cols[waveNumber]
            logging.debug('grouping by cols: ' + str(groupBy))
            waveDf.groupby(groupBy, as_index=False).mean()

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

    def __init__(self, label, all_cols):
        super(MotherVar, self).__init__(label, all_cols)

    def isMother(self):
        return True

    def isChild(self):
        return False

    def getSubjectPrefix(self):
        return 'Mother'


class ChildVar(SubjectVar):

    __metaclass__ = ABCMeta

    def __init__(self, label, all_cols):
        super(ChildVar, self).__init__(label, all_cols)

    def isMother(self):
        return False

    def isChild(self):
        return True

    def getSubjectPrefix(self):
        return 'Child'
