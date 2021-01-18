import logging
from step1_createDataSet.varsColsPerWaveFactory import VarColsPerWaveFactory
from step1_createDataSet.varsStrcture.subjectVar import MotherVar, SubjectsVarsEnum


def config():
    logging.basicConfig(level=logging.DEBUG)


def main():
    config()
    msg = "hello thesis"
    print(msg)
    colsPerWaves = VarColsPerWaveFactory()
    motherOrganismicFaith = MotherVar(
        SubjectsVarsEnum.OrganismicFaith.value, colsPerWaves.getColsForWaves(SubjectsVarsEnum.OrganismicFaith.name))


main()
