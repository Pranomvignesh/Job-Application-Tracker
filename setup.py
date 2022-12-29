from setuptools import setup, find_packages
setup(
  name="JobApplicationTracker",
  description="A Python CLI to track my application progress",
  version="0.0.0",
  packages=find_packages(),
  author="Vignesh Prakash",
  author_email="pranomvignesh@gmail.com",
  url="https://github.com/Pranomvignesh/Job-Application-Tracker",
  install_requires = [],
  entry_points = '''
  [console_scripts]
  addJob=JobApplicationTracker:addJob
  updateJob=JobApplicationTracker:updateJob
  '''
)