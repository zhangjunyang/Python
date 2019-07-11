import dicom
import json
import  os
def loadFileInformation(filename):
    information = {}
    ds = dicom.read_file(filename)
    information['w'] = ds.Rows
    information['h'] = ds.Columns
    information['type'] = ds.Modality
    information['PatientBirthDate'] = ds.PatientBirthDate
    information['PatientSex'] = ds.PatientSex
    information['StudyID'] = ds.StudyID
    information['StudyDate'] = ds.StudyDate
    information['StudyTime'] = ds.StudyTime
    information['SOP Instance UID '] = ds.SOPInstanceUID
    information['Manufacturer'] = ds.Manufacturer
    print (dir(ds))
    print (type(information))
    return information
path = "E:\\image\\xxx.dcm"
a=loadFileInformation(path)
print (a)