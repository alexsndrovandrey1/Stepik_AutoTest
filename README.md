# Stepik_AutoTest

Репозиторий с практическими заданиями по автоматизации тестирования с помощью **Selenium WebDriver (Python)** в рамках курса Stepik.

## 📋 Описание

Здесь собраны скрипты, которые решают конкретные задачи автоматизации на тестовых страницах [`suninjuly.github.io`](https://suninjuly.github.io). Код наглядно демонстрирует базовые возможности Selenium: поиск элементов, работу с формами, обработку всплывающих окон, загрузку файлов, таймауты и ожидания.

## 📁 Структура проекта

### 1. [Знакомство с Selenium](Знакомство%20с%20Selenium/)
Первые шаги: базовый поиск элементов и работа с простыми формами.

| Файл | Тема |
|------|------|
| [`lesson6_step4.py`](Знакомство%20с%20Selenium/lesson6_step4.py) | Поиск по `NAME`, `CLASS_NAME`, `ID`, `CSS_SELECTOR`, заполнение формы |
| [`lesson6_step5.py`](Знакомство%20с%20Selenium/lesson6_step5.py) | Поиск ссылки по тексту `LINK_TEXT` (вычисление значения через `math`) |
| [`lesson6_step7.py`](Знакомство%20с%20Selenium/lesson6_step7.py) | Поиск группы элементов `TAG_NAME` и заполнение большой формы в цикле |
| [`lesson6_step8.py`](Знакомство%20с%20Selenium/lesson6_step8.py) | Поиск кнопки по `XPATH` |
| [`lesson6_step10.py`](Знакомство%20с%20Selenium/lesson6_step10.py) | Проверка успешной регистрации через `assert` (registration1) |
| [`lesson6_step11.py`](Знакомство%20с%20Selenium/lesson6_step11.py) | Аналогичная проверка регистрации (registration2, намеренно с ошибкой для отладки) |

### 2. [Полезные методы Selenium](Полезные%20методы%20Selenium/)
Продвинутые приёмы: вычисление ответов, работа с атрибутами, выпадающими списками, окнами и загрузкой файлов.

| Файл | Тема |
|------|------|
| [`lesson1_step5.py`](Полезные%20методы%20Selenium/lesson1_step5.py) | Чтение значения из элемента, расчёт ответа, чекбокс и радиокнопка |
| [`lesson1_step7.py`](Полезные%20методы%20Selenium/lesson1_step7.py) | Получение значения через `get_attribute()`, валидация капчи |
| [`lesson2_step6.py`](Полезные%20методы%20Selenium/lesson2_step6.py) | Выполнение JavaScript `execute_script()` для прокрутки страницы |
| [`lesson2_spet3.py`](Полезные%20методы%20Selenium/lesson2_spet3.py) | Работа с выпадающим списком через класс `Select` |
| [`lessin2_step8.py`](Полезные%20методы%20Selenium/lessin2_step8.py) | Загрузка файла на странице (`send_keys` + сборка пути через `os`) |
| [`lesson3_step4.py`](Полезные%20методы%20Selenium/lesson3_step4.py) | Работа с модальными окнами `alert` (`switch_to.alert`, `accept()`) |
| [`lesson3_step6.py`](Полезные%20методы%20Selenium/lesson3_step6.py) | Переключение между вкладками (`switch_to.window`) |
| [`lesson4_step8.py`](Полезные%20методы%20Selenium/lesson4_step8.py) | Явные ожидания `WebDriverWait` + `expected_conditions` (`EC`) |

## 🚀 Установка и запуск

1. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Убедитесь, что у вас установлен [chromedriver](https://chromedriver.chromium.org/), совместимый с вашей версией Chrome (для Selenium 4 он запускается автоматически).

3. Запустите любой скрипт:

   ```bash
   python "Знакомство с Selenium/lesson6_step4.py"
   ```

## 📦 Зависимости

Основные пакеты (см. [`requirements.txt`](requirements.txt)):

- `selenium==4.48.0` — фреймворк для автоматизации браузера
- Остальные пакеты — транзитивные зависимости Selenium (`attrs`, `certifi`, `PySocks`, `trio`, `outcome` и т.д.)

## 🧩 Используемые техники

- Поиск элементов: `By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.TAG_NAME`, `By.CSS_SELECTOR`, `By.LINK_TEXT`, `By.XPATH`
- Ввод данных: `send_keys()`, `click()`
- Работа с выпадающими списками: `Select`
- Работа с окнами браузера: `alert`, `window_handles`
- Загрузка файлов и сборка путей через `os.path`
- Выполнение JavaScript: `execute_script()`
- Явные и неявные ожидания: `WebDriverWait`, `expected_conditions`
- Проверка результатов с помощью `assert`

## 🛠 Дополнительные материалы

- [`CSS - омбинированные селекторы.webp`](CSS%20-%20омбинированные%20селекторы.webp) — шпаргалка по CSS-селекторам
- [`Полезные методы Selenium/test.txt`](Полезные%20методы%20Selenium/test.txt) — тестовый файл для задания по загрузке файлов