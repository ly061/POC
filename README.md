## Install Allure on windows

* first, install scoop, open powershell command line. input `iwr -useb get.scoop.sh | iex`
* then install allure `scoop install allure`


## Allure command line.

* first, pytest generate allure json data `pytest --alluredir=report/xml`
* second, use `allure` command line generate allure report `allure generate report/allure/ -o report/allure-report/ --clean`
* last, check allure report `allure open -h 127.0.0.1 -p 8080 report/allure-report`
* allure serve `allure serve report/allure`
