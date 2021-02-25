import pandas
import logging
import pathlib
import os
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils
from step1_createDataSet.varsColsPerWaveFactory import VarColsPerWaveFactory
from step1_createDataSet.varsStrcture.subjectVar import ChildVar, MotherVar, FatherVar
from dotenv import load_dotenv


def config():
    logging.basicConfig(level=logging.DEBUG)
    load_dotenv()
    logging.debug('os.getenv("RAW_DATA_FOLDER") =' +
                  str(os.getenv("RAW_DATA_FOLDER")))
    rawDataFolderPath = os.getenv("RAW_DATA_FOLDER") if os.getenv(
        "RAW_DATA_FOLDER") != '' else '\\step1_createDataSet\\rawData\\'

    CreateDataSetUtils.rawDataFolder = str(
        pathlib.Path().absolute()) + rawDataFolderPath

    outputDataFolderPath = os.getenv("OUTPUT_DATA_FOLDER") if os.getenv(
        "OUTPUT_DATA_FOLDER") != '' else '\\step1_createDataSet\\output\\'

    CreateDataSetUtils.outputDataFolder = str(
        pathlib.Path().absolute()) + outputDataFolderPath

    logging.info('Readind Raw Data Folder from :' +
                 CreateDataSetUtils.rawDataFolder)

    CreateDataSetUtils.indexColName = os.getenv("INDEX_COL_NAME") if os.getenv(
        "INDEX_COL_NAME") != '' else 'family'

    CreateDataSetUtils.createIndexFile(CreateDataSetUtils.indexColName, CreateDataSetUtils.getRawDataFolder(
    ) + '\\wave1.csv'

    )


def createDatasetForMainVars(colsPerWaves):
    dfMainVars = pandas.DataFrame()
    dfMainVars[CreateDataSetUtils.indexColName] = CreateDataSetUtils.getIndex()
    fullMapping = colsPerWaves.getAllVarsMapping()
    for subjectVarKey in fullMapping:
        subjectVar = fullMapping[subjectVarKey]
        logging.info('Creating dataset for main var: ' + str(subjectVarKey))
        mainVar = pandas.Series()
        if subjectVar["type"] == "Mother":
            mainVar = MotherVar(
                subjectVarKey, colsPerWaves.getColsForWaves(subjectVarKey), CreateDataSetUtils.getIndexColName())

        if subjectVar["type"] == "Father":
            mainVar = FatherVar(
                subjectVarKey, colsPerWaves.getColsForWaves(subjectVarKey), CreateDataSetUtils.getIndexColName())

        if subjectVar["type"] == "Child":
            mainVar = ChildVar(
                subjectVarKey, colsPerWaves.getColsForWaves(subjectVarKey), CreateDataSetUtils.getIndexColName())
        dfMainVars[subjectVarKey] = mainVar.mean
        dfMainVars.to_csv(str(pathlib.Path().absolute()) +
                          '\\step1_createDataSet\\output\\MeansOfMainVarsAcrossAllWaves.csv')
    print(dfMainVars)


def main():
    config()
    msg = "hello thesis"
    print(msg)
    createDatasetForMainVars(VarColsPerWaveFactory())


main()
