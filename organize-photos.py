import argparse
import re
import os
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description='Organize files with a YYYYMMDD name format into yearly and monthly folders in a destination directory.')
parser.add_argument('source', help='The folder that contains the files to organize')
parser.add_argument('destination', help='The main folder that contains the destination folder organization')
args = parser.parse_args()

sourcePath = Path(args.source)
if not sourcePath.exists() or not sourcePath.is_dir():
  print('Source directory does not exist')
  exit(1)

destinationPath = p = Path(args.destination)
if not destinationPath.exists() or not destinationPath.is_dir():
  print('Destination directory does not exist')
  exit(1)
  
for sourceFile in sourcePath.iterdir():
  if not sourceFile.is_file:
    continue
  
  regexMatch = re.search('(\d{4})(\d{2})(\d{2})\_.*', sourceFile.name)
  if regexMatch is None:
    print(f'File ignored: {sourceFile.name}')
    continue

  year = regexMatch.group(1)
  month = regexMatch.group(2)
  day = regexMatch.group(3)

  yearDir = destinationPath / year
  if not yearDir.exists():
    os.mkdir(yearDir)
  
  monthDir = yearDir / month
  if not monthDir.exists():
    os.mkdir(monthDir)

  destinationFile = monthDir/sourceFile.name
  shutil.move(sourceFile, destinationFile)
  print(f'Moved {sourceFile} to {destinationFile}')

print('Complete!')
