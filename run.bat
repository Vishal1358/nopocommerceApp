pytest -v -n=2 -m "sanity" --html=./Report/report.html testCases/ --browser chrome
pytest -v -m "data1" --html=./Report/report.html testCases/ --browser chrome
pytest -v -m "data2" --html=./Report/report.html testCases/ --browser chrome
pytest -v -m "regression" --html=Report/report.html testCases/ --browser chrome
pytest -v -m "sanity or regression" --html=Report/report.html testCases/ --browser chrome
pytest -v -m "sanity and regression" --html=Report/report.html testCases/ --browser chrome
