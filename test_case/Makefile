.SILENT:

migrate:
	@python3 manage.py makemigrations && python3 manage.py migrate

runlocal:
	@export DJANGO_SETTINGS_MODULE=test_case.settings.local && \
	make migrate && \
	python3 manage.py runserver

runprod:
	@export DJANGO_SETTINGS_MODULE=test_case.settings.prod && \
	make migrate && \
	python3 manage.py runserver