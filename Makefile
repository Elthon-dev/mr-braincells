.PHONY: install run setup clean

install:
	./install.sh

run:
	python3 src/main.py

setup-termux:
	./setup-termux.sh

clean:
	rm -rf __pycache__ */__pycache__ */*/__pycache__ *.db
