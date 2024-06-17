local_test:
	pytest
	flake8 .

create_container:
	docker build -t template-api:v1 .

run_container_local:
	docker run -p 8080:8080 --env-file .env template-api:v1
