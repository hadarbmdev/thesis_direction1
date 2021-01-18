import logging
import pathlib
import os
from step1_createDataSet.createDataSetUtils import CreateDataSetUtils
from step1_createDataSet.varsColsPerWaveFactory import VarColsPerWaveFactory
from step1_createDataSet.varsStrcture.subjectVar import ChildVar, MotherVar
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
    logging.info('Readind Raw Data Folder from :' +
                 CreateDataSetUtils.rawDataFolder)

    CreateDataSetUtils.indexColName = os.getenv("INDEX_COL_NAME") if os.getenv(
        "INDEX_COL_NAME") != '' else 'family'


def createDatasetForMainVars(colsPerWaves):
    fullMapping = colsPerWaves.getAllVarsMapping()
    for subjectVarKey in fullMapping:
        subjectVar = fullMapping[subjectVarKey]
        logging.info('Creating dataset for main var: ' + str(subjectVarKey))
        if subjectVar["type"] == "Mother":
            MotherVar(
                subjectVarKey, colsPerWaves.getColsForWaves(subjectVarKey), CreateDataSetUtils.getIndexColName())

        if subjectVar["type"] == "Child":
            ChildVar(
                subjectVarKey, colsPerWaves.getColsForWaves(subjectVarKey), CreateDataSetUtils.getIndexColName())


def main():
    config()
    msg = "hello thesis"
    print(msg)
    createDatasetForMainVars(VarColsPerWaveFactory())


main()
