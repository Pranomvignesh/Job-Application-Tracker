import os
import inquirer

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Constants
FOLDER_PATH = os.getenv('FOLDER_PATH')
EXCEL_FILE_NAME = os.getenv('EXCEL_FILE_NAME')

def addJob():
  questions = [
    inquirer.Text(
      'CompanyName',
      message="Enter the Company name"
    ),
    inquirer.Text(
      'JobTitle',
      message="Enter the Job Title"
    ),
    inquirer.List(
      "resumeType",
      message="Select the Resume Type to start",
      choices=[
        "Machine Learning Resume",
        "Software Developer Resume",
        "Complete Resume"
      ]
    )
  ]
  answers = inquirer.prompt(questions)
  print(answers)

def updateJob():
  print('update job')