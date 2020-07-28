#!/usr/bin/env python3
import os
import re
import sys

pathToFile = sys.argv[1]
def getScannerQubeAnalysisFile():
  pattern = r'\(SonarQube analysis\)[\s\S]*\(Saving Logs\)'
  pattern2 = r'waitForQualityGate[\s\w\'.-]*'
  errorpattern = r'ERROR[:\s\w]+'
  fileName = pathToFile.split('/')[-1]
  newFileName = "Sonar-analysis-"+fileName
  match = ''
  try:
    with open(pathToFile, 'r') as f:
      data = f.read()
      match = re.findall(pattern, data, flags=0)[0]
      match2 = re.findall(pattern2, match, flags=0)[0].split("\n")
      errors = re.findall(errorpattern, match, flags=0)
      finalData = "\n".join(match2[1:-1])+"\n"+"\n".join(errors)
      print(finalData)

    with open(newFileName, "w") as f:
    # Writing data to a file
      f.write(finalData)
  except:
    print("Unexpected error:", sys.exc_info()[0])

if __name__=="__main__":
  getScannerQubeAnalysisFile()
