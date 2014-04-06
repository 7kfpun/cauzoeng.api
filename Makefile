APPLICATION=$(shell grep "application: " app.yaml | cut -d' ' -f 2)
GAE=$(shell find /opt/google_appengine_* -maxdepth 0 -type d | sort -r | head -1)

APP_PATH=.
LOCALE=en_US zh_TW zh_CN th_TH

all:
	@git submodule update --init --recursive
	@git submodule foreach --recursive git pull origin master

# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

# target: t - Run tests
.PHONY: t
t: clean
	nosetests -v --with-gae --gae-lib-root=$(GAE)

# target: run - Run application server
.PHONY: run
run:
	$(GAE)/dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --automatic_restart --log_level=debug --enable_sendmail=yes $(APP_PATH) --skip_sdk_update_check

# target: upload - Upload the App
.PHONY: update
update:
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver update $(APP_PATH)

# target: update_queues - Update Task Queue Configuration
.PHONY: update_queues
update_queues:
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver update_queues $(APP_PATH)
                     
# target: update_dos - Update the DoS Protection Configuration
.PHONY: update_dos
update_dos:
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver update_dos $(APP_PATH)

# target: update_cron - Manage Scheduled Tasks
.PHONY: update_cron
update_cron:
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver update_cron $(APP_PATH)

# target: cron_info - Displays a summary of the scheduled task configuration
.PHONY: cron_info
cron_info:
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver appcfg cron_info $(APP_PATH)

# target: request_logs - Download Logs
.PHONY: request_logs
request_logs:
	@echo "Downloading Logs"
	$(GAE)/appcfg.py --oauth2 --noauth_local_webserver request_logs $(APP_PATH) appengine.log
                    
# target: extract_locale - Extract language files
.PHONY: extract_locale
extract_locale:
	pybabel extract -F ./locale/babel.cfg -o ./locale/messages.pot ./

# target: init_locale - Initialize language files
.PHONY: init_locale
init_locale:
	for locale in $(LOCALE) ; do \
	    pybabel init -l $$locale -d ./locale -i ./locale/messages.pot ; \
	done

# target: update_locale - Update language files
.PHONY: update_locale
update_locale:
	for locale in $(LOCALE) ; do \
	    pybabel update -l $$locale -d ./locale -i ./locale/messages.pot ; \
	done

# target: compile_locale - Compile language files
.PHONY: compile_locale
compile_locale:
	pybabel compile -f -d ./locale

# target: lupdate - Update all locale files
.PHONY: lupdate
lupdate: extract_locale update_locale compile_locale

# target: download_contact
.PHONY: download_contact
	$(GAE)/bulkloader.py --download --url http://$(APPLICATION).appspot.com/_ah/remote_api --config_file generated_bulkloader.yaml --kind=Contact --filename downloads/download_contact.csv

# target: clean - Clean all .pyc
.PHONY: clean
clean:
	rm -f *.py[co] *.orig
	rm -f */*.py[co] */*.orig

# target: generate_docs - Generate document files
.PHONY: generate_docs
generate_docs:
	mkdir -p docs
	$(GAE)/endpointscfg.py get_discovery_doc cauzoeng.api.LotteryApi -o docs

# target: generate_client - Generate android client library
.PHONY: generate_client
generate_client:
	$(GAE)/endpointscfg.py get_client_lib java cauzoeng.api.LotteryApi
