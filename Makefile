# This file is intended to help with testing
# DxSter, the Alzheimer's Algortihmic Diagnostic Helper.
# Some elements reused from redi/vagrant/Makefile.

MAKE_CONFIG_FILE := Makefile.conf
CONFIG_FOLDER        := $(shell cat ${MAKE_CONFIG_FILE} | sed -e 's/ //g' | grep -v '^\#' | grep 'config_folder=' | cut -d '=' -f2)
CONFIG_FILE          := $(CONFIG_FOLDER)/settings.conf

# Makefile examples
# REDCAP_VM_TOKEN := $(shell cat ${CONFIG_FILE} | sed -e 's/ //g' | grep -v '^\#' | grep 'token=' | cut -d '=' -f2)
# REDCAP_API_URI := $(shell cat ${CONFIG_FILE} | sed -e 's/ //g' | grep -v '^\#' | grep 'redcap_uri=' | cut -d '=' -f2)
# REDCAP_RECORDS_CMD:=$(REDCAP_RECORDS_PROGRAM) --token=$(REDCAP_VM_TOKEN) --url=$(REDCAP_API_URI)
#FAKE_DATA_FILE = patient_data.txt
#FAKE_ENROLLMENT_FILE = fake_enrollment.txt

help:
	@echo "\n Available tasks:"
	@echo "\t clean - Hey you, your cleanup function can go here."
	@echo "\t init - install all python package requirement from the requirements.txt file."
	@echo "\t test - use nosetests to run all unit tests in the /tests folder."
	@echo "\t serve - use the python SimpleHTTPServer to run a local demo site"

#rc_fake_enrollment:
# $(REDCAP_RECORDS_CMD) -i $(FAKE_ENROLLMENT_FILE)
#rc_fake_dates:
#	$(REDCAP_RECORDS_CMD) -i $(FAKE_DATA_FILE)



clean:
	# get rid of  old files

	#-rm -rf *_output.csv
	#-rm -rf 'preproc/scenario100/raw.csv'

#run_test_small:
	# use the small test data files in the test folder
	#make clean && ./preproc/mergeNcsvfiles.py -f 'preproc/scenario100/' --debug && cat *_output.csv


init:
	pip install -r requirements.txt

test:
	nosetests tests

serve:
	bash scripts/serve.sh scripts/config.ini
