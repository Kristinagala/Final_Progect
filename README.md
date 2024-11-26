# Final_Progect

## Дипломная работа по автоматизации тестирования

### Примечание:
В UI тестах увеличен тайм-аут до 15 секунд. Это связанно с тем, что при 
выполнении теста эпизодически появляется CAPTCHA, которую, как я поняла 
обойти нельзя. Поэтому при выполнении UI тестов время от времени нужно вручную
потдверждать КиноПоиску, что я не робот, что бы тест не упал.


### Шаги
1. Склонировать проект 'git clone https://github.com/Kristinagala/Final_Progect.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

Для запуска теста используйте команду:
```
pytest --alluredir=./allure-result
```
Для просмотра отчета используйте команду:
```
allure serve allure-result/
```

Для генерации отчета используйте команду:
```
allure generate allure-result -o allure-report
```
Для просмотра отчета используйте команду:
```
allure open allure-report
```

### Стек:
- pytest
- selenium
- webdriver-manager 
- requests
- allure-pytest
- configparser
- json


### Структура:
- ./test - тесты
- ./page - описание страниц
- ./api - хелперы для работы с API
- ./configuration - провайдер настроек
   - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
   - test_data.json - тестовые данные



### Запуск тестов:
- Запуск только UI-тестов,
- Запуск только API-тестов,
- Запуск всех тестов

### Библиотеки
- pip3 install pytest
- pip install selenium
- pip install webdriver-manager 
- pip install allure-pytest
- pip install requests

- [Финальный проект по ручному тестированию](https://www.notion.so/4b232c4972ee4b3da80a719c4bce7ce5)
kristinagalanceva917@gmail.com
888Kristi888