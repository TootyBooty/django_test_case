.SILENT:

startlocal:
	@export DJANGO_SETTINGS_MODULE=test_case.settings.local && \
	docker-compose up -d --build

startprod:
	@export DJANGO_SETTINGS_MODULE=test_case.settings.prod && \
	docker-compose up -d --build