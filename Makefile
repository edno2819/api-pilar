local_test:
	pytest
	flake8 .

create_container:
	docker build -t template-api .

run_container_local:
	docker run -p 8080:8080 --env-file .env template-api