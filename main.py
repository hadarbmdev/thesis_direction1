import logging
from step1_createDataSet.varsColsPerWaveFactory import VarColsPerWaveFactory
from step1_createDataSet.varsStrcture.subjectVar import MotherVar, SubjectsVarsEnum


def config():
    logging.basicConfig(level=logging.DEBUG)


def main():
    config()
    msg = "hello thesis"
    print(msg)
    motherOrganismicFaith = MotherVar(
        SubjectsVarsEnum.OrganismicFaith.value, VarColsPerWaveFactory.getColsForWaves(SubjectsVarsEnum.OrganismicFaith.name))


main()
