#! /usr/bin/python3

import argparse
from datetime import date, timedelta
import re
import os
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description='''
Copy files from last month's directory (with format YYYY-MM) in the source into a YYYY/MM folder in the destination directory.
This should be run on a monthly cadence.
''')
parser.add_argument('source', help='The folder that contains the files to organize')
parser.add_argument('destination', help='The main folder that contains the destination folder organization')
args = parser.parse_args()

sourcePath = p = Path(args.source)
if not sourcePath.exists() or not sourcePath.is_dir():
  print('Source directory does not exist')
  exit(1)

destinationPath = p = Path(args.destination)
if not destinationPath.exists() or not destinationPath.is_dir():
  print('Destination directory does not exist')
  exit(1)

# Should reliably get the previous month. This should be run on a `@monthly` cron job.
lastMonthDate = date.today() - timedelta(days=27)
sourceDirName = f'{lastMonthDate.year}-{lastMonthDate.month}'
sourceDir = sourcePath / sourceDirName

yearDir = destinationPath / f'{lastMonthDate.year}'
if not yearDir.exists():
  os.mkdir(yearDir)

monthDir = yearDir / f'{lastMonthDate.month}'
if not monthDir.exists():
  os.mkdir(monthDir)

shutil.copytree(sourceDir, monthDir, dirs_exist_ok=True)
print(f'Moved {sourceDir} to {monthDir}')

print('Complete!')
