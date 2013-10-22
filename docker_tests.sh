# Create virtualenv
virtualenv venv
# Activate virtualenv
. venv/bin/activate
# Install libraries
pip install -r requirements.txt
# Remove files generated in the previous build
rm -f .coverage coverage.xml nosetests.xml
# Execute tests
nosetests --with-doctest --with-xunit --with-coverage --cover-xml --cover-package=config_reader
