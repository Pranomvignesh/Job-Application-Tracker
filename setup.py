from setuptools import setup, find_packages
setup(
  name = "JobApplicationTracker",
  version = "0.0.0",
  packages=find_packages(),
  author="pranomvignesh@gmail.com",
  install_requires = [],
  entry_points = '''
  [console_scripts]
  job=JobApplicationTracker:JobApplicationTracker
  '''
)
