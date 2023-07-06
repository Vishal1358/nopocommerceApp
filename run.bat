pytest -s -v -m "sanity" --html=./Report/report.html testCases/ --browser chrome
rem pytest -v -m "regression" --html=./Report/report.html testCase/ --browser chrome
rem pytest -v -m "sanity or regression" --html=./Report/report.html testCase/ --browser chrome
rem pytest -v -m "sanity and regression" --html=./Report/report.html testCase/ --browser chrome