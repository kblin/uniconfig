unit:
	py.test -v

coverage:
	py.test --cov=uniconfig --cov-report=html --cov-report=term-missing

dist:
	python setup.py sdist bdist_wheel
	twine upload dist/*
