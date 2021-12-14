run:
	docker-compose run --rm app bash -c "make install; time IS_PREPARED=true python3 scripts/query.py";
	docker-compose run --rm app bash -c "make install; time python3 scripts/query.py";
