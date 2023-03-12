# JDBC_to_SQLAlchemyTranslator

<p><a href="#anchor1">Russian</a></p>
<p><a href="#anchor2">Polski (automatyczne tłumaczenie)</a></p>
<p><a href="#anchor3">English (automatic translation)</a></p>


<p id="anchor1"></p>
<h2>Russian</h2>
<p>
Функция трансляции инициализирующей строки подключения к базе данных из Java в Python

На вход подается строка java, на выходе получаем строку для Python.
Работает универсально для всех типов баз, но необходимо заполнить словари сопоставления. На данный момент
сопоставления только для PostgreSQL


Словарь _db_types содержит сопоставления для БД. Ключ - название базы в Java, значение - в Python
Словарь _parametrs содержит сопоставления параметров. Аналогичен _db_types
</p>

<p id="anchor2"></p>
<h2>Polski</h2>
<p>
Funkcja tłumaczenia inicjalizującego ciągu połączenia z bazą danych z Java do Pythona

Ciąg java jest podawany do wejścia, na wyjściu otrzymujemy ciąg dla Pythona.
Działa uniwersalnie dla wszystkich typów baz, ale należy wypełnić słowniki mapowania. Na razie
mapowania tylko dla PostgreSQL


Słownik _db_types zawiera mapowania dla bazy danych. Klucz to nazwa bazy w Javie, wartość w Pythonie
Słownik _parameters zawiera mapowania parametrów. Podobne do _db_types</p>

<p id="anchor3"></p>
<h2>English</h2>
<p>Translation function of initializing database connection string from Java to Python

The input is a java string, and the output is a string for Python.
It works universally for all types of databases, but it is necessary to fill in matching dictionaries. At the moment
, the mappings are only for PostgreSQL


The _db_types dictionary contains mappings for the database. The key is the name of the database in Java, the value is in Python
The _parameters dictionary contains parameter mappings. Similar to _db_types</p>
