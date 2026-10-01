# Source: synthetic Synthea patient bundles from a data engineering take-home assessment
#source2: https://www.kaggle.com/code/drscarlat/fhir-starter-parse-healthcare-bundles-into-tables/notebook

import json
import pandas as pd
import os

import numpy as np  
from datetime import date
from tqdm.auto import tqdm
tqdm.pandas()

from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
from fhir.resources.condition import Condition
from fhir.resources.observation import Observation
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.procedure import Procedure
from fhir.resources.encounter import Encounter
from fhir.resources.claim import Claim
from fhir.resources.immunization import Immunization



filesList = os.listdir('./data')
print(len(filesList))

PATIENT = pd.DataFrame(columns=['PatientUID', 'NameFamily', 'NameGiven', 'DoB', 'Gender'])
CONDITION = pd.DataFrame(columns=['ConditionText', 'ConditionOnsetDates', 'PatientUID'])
OBSERVATION = pd.DataFrame(columns=['ObservationText', 'ObservationValue', 'ObservationUnit','ObservationDate', 'PatientUID'])
MEDICATION = pd.DataFrame(columns=['MedicationText', 'MedicationDates', 'PatientUID'])
PROCEDURE = pd.DataFrame(columns=['ProcedureText', 'ProcedureDates', 'PatientUID'])
ENCOUNTER = pd.DataFrame(columns=['EncountersText', 'EncounterLocation', 'EncounterProvider','EncounterDates', 'PatientUID'])
CLAIM = pd.DataFrame(columns=['ClaimProvider', 'ClaimInsurance', 'ClaimDate', 'ClaimType','ClaimItem', 'ClaimUSD', 'PatientUID'])
IMMUNIZATION = pd.DataFrame(columns=['Immunization', 'ImmunizationDates', 'PatientUID'])


first = input("Enter the first name of the patient (including three numbers with no spaces): ")

last = input("Enter the last name of the patient (including three numbers with no spaces): ")

path = 'data/'
find = str(first) + '_' + str(last)

for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and find in i:
        print(i)
        f = open(path+i)
        break

json_obj = json.load(f)

oneBundle = Bundle.parse_obj(json_obj)

# Resources
resources = []
if oneBundle.entry is not None:
    for entry in oneBundle.entry:
        resources.append(entry.resource)

oneResources = []
for j in range(len(resources)):
    oneResources.append(type(resources[j]))
    
print(len(oneResources))

uniqResources = set(oneResources)
print(len(uniqResources))
uniqResources

onePatient = Patient.parse_obj(resources[0])
onePatient.name[0]

# Patient demographics
onePatientID = onePatient.id

print("ID: "+onePatientID)
print("Family Name: "+onePatient.name[0].family)
print("Given Name: "+onePatient.name[0].given[0])
print("Date of Birth: "+ str(onePatient.birthDate))
print("Gender: "+onePatient.gender)

def Conditions():
    try:
        resCondition = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Condition':
                resCondition.append(resources[j])
                
        conditions = []
        conditionOnsetDates = []
        for j in range(len(resCondition)):
            oneCondition = Condition.parse_obj(resCondition[j])
            conditions.append(oneCondition.code.text)
            conditionOnsetDates.append(str(oneCondition.onsetDateTime.date()))  
            
        onePatConditions = pd.DataFrame()

        onePatConditions['ConditionText'] = conditions
        onePatConditions['ConditionOnsetDates'] = conditionOnsetDates
        onePatConditions['PatientUID'] = onePatientID

        print(onePatConditions.shape)
        print(onePatConditions.sample(onePatConditions.shape[0]).sort_index())
    except:
        print("No Condition resources")

def Observations():
    try:
        resObservation = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Observation':
                resObservation.append(resources[j])
                
        obsText = []
        obsValue = []
        obsUnit = []
        obsDate = []

        for j in range(len(resObservation)):
            oneObservation = Observation.parse_obj(resObservation[j])
            obsText.append(oneObservation.code.text)
            if oneObservation.valueQuantity:
                obsValue.append(round(oneObservation.valueQuantity.value,2))
                obsUnit.append(oneObservation.valueQuantity.unit)
            else:
                obsValue.append('None')
                obsUnit.append('None')
            obsDate.append(oneObservation.issued.date())
        onePatObs = pd.DataFrame()

        onePatObs['ObservationText'] = obsText
        onePatObs['ObservationValue'] = obsValue
        onePatObs['ObservationUnit'] = obsUnit
        onePatObs['ObservationDate'] = obsDate
        onePatObs['PatientUID'] = onePatientID

        print(onePatObs.shape)
        print(onePatObs.sample(onePatObs.shape[0]).sort_index())
    except:
        print("No Observation resources")
        
def Medications():
    try:
        resMedicationRequest = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'MedicationRequest':
                resMedicationRequest.append(resources[j])
                
        meds = []
        medsDates = []
        for j in range(len(resMedicationRequest)):
            oneMed = MedicationRequest.parse_obj(resMedicationRequest[j])
            meds.append(oneMed.medicationCodeableConcept.text)
            medsDates.append(str(oneMed.authoredOn.date()))  
            
        onePatMeds = pd.DataFrame()

        onePatMeds['MedicationText'] = meds
        onePatMeds['MedicationDates'] = medsDates
        onePatMeds['PatientUID'] = onePatientID

        print(onePatMeds.shape)
        print(onePatMeds.sample(onePatMeds.shape[0]).sort_index())
    except:
        print("No MedicationRequest resources")

def Procedures():
    try:
        resProcedures = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Procedure':
                resProcedures.append(resources[j])
                
        procs = []
        procDates = []
        for j in range(len(resProcedures)):
            oneProc = Procedure.parse_obj(resProcedures[j])
            procs.append(oneProc.code.text)
            procDates.append(str(oneProc.performedPeriod.start.date()))  
            
        onePatProcs = pd.DataFrame()

        onePatProcs['ProcedureText'] = procs
        onePatProcs['ProcedureDates'] = procDates
        onePatProcs['PatientUID'] = onePatientID

        print(onePatProcs.shape)
        print(onePatProcs.sample(onePatProcs.shape[0]).sort_index())
    except:
        print("No Procedure resources")

def Encounters():
    try:
        resEncounters = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Encounter':
                resEncounters.append(resources[j])
                
        encounters = []
        encountDates = []
        encountLocation = []
        encountProvider = []

        for j in range(len(resEncounters)):
            oneEncounter = Encounter.parse_obj(resEncounters[j])
            encounters.append(oneEncounter.type[0].text)
            encountLocation.append(oneEncounter.serviceProvider.display)
            if oneEncounter.participant:
                encountProvider.append(oneEncounter.participant[0].individual.display)
            else:
                encountProvider.append('None')
            encountDates.append(str(oneEncounter.period.start.date()))  
            
        onePatEncounters = pd.DataFrame()

        onePatEncounters['EncountersText'] = encounters
        onePatEncounters['EncounterLocation'] = encountLocation
        onePatEncounters['EncounterProvider'] = encountProvider
        onePatEncounters['EncounterDates'] = encountDates
        onePatEncounters['PatientUID'] = onePatientID

        print(onePatEncounters.shape)
        print(onePatEncounters.sample(onePatEncounters.shape[0]).sort_index())
    except:
        print("No Encounter resources")

def Claims():
    try:
        resClaims = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Claim':
                resClaims.append(resources[j])
                
        claimProvider = []
        claimInsurance = []
        claimDate = []
        claimType = []
        claimItem = []
        claimUSD = []

        for j in range(len(resClaims)):
            oneClaim = Claim.parse_obj(resClaims[j])
            # Inner loop over claim items:
            for i in range(len(resClaims[j].item)):
                claimProvider.append(oneClaim.provider.display)
                claimInsurance.append(oneClaim.insurance[0].coverage.display)
                claimDate.append(str(oneClaim.billablePeriod.start.date()))
                claimType.append(oneClaim.type.coding[0].code)
                claimItem.append(resClaims[j].item[i].productOrService.text)
                if resClaims[j].item[i].net:
                    claimUSD.append(str(resClaims[j].item[i].net.value))
                else:
                    claimUSD.append('None')
            
        onePatClaims = pd.DataFrame()

        onePatClaims['ClaimProvider'] = claimProvider
        onePatClaims['ClaimInsurance'] = claimInsurance
        onePatClaims['ClaimDate'] = claimDate
        onePatClaims['ClaimType'] = claimType
        onePatClaims['ClaimItem'] = claimItem
        onePatClaims['ClaimUSD'] = claimUSD
        onePatClaims['PatientUID'] = onePatientID

        print(onePatClaims.shape)
        print(onePatClaims.sample(onePatClaims.shape[0]).sort_index())
    except:
        print("No Claim resources")

def Immunizations():
    try:
        resImmunization = []
        for j in range(len(resources)):
            if resources[j].__class__.__name__ == 'Immunization':
                resImmunization.append(resources[j])
                
        immun = []
        immunDates = []
        for j in range(len(resImmunization)):
            oneImmun = Immunization.parse_obj(resImmunization[j])
            immun.append(oneImmun.vaccineCode.coding[0].display)
            immunDates.append(str(oneImmun.occurrenceDateTime.date()))  
            
        onePatImmun = pd.DataFrame()

        onePatImmun['Immunization'] = immun
        onePatImmun['ImmunizationDates'] = immunDates
        onePatImmun['PatientUID'] = onePatientID

        print(onePatImmun.shape)
        print(onePatImmun.sample(onePatImmun.shape[0]).sort_index())
    except:
        print("No Immunization resources")

n = ' '
while n != 'q':
    print("\n\n\n")
    print("Select which type of data you want to see:")
    print("1. Conditions")
    print("2. Observations")
    print("3. Medications")
    print("4. Procedures")
    print("5. Encounters")
    print("6. Claims")
    print("7. Immunizations")
    print("8. Change Patient under maintenece")
    print("q. Quit")
    n = input("Enter your choice: ")
    print("\n\n\n")
    if n == '1':
        Conditions()
    elif n == '2':
        Observations()
    elif n == '3':
        Medications()
    elif n == '4':
        Procedures()
    elif n == '5':
        Encounters()
    elif n == '6':
        Claims()
    elif n == '7':
        Immunizations()
    elif n == 'q':
        print("Quitting...")
