Test automatyczny napisany w Windows10 z wykorzystaniem:
- Python 3.8.2
- Pytest 6.2.5
- Selenium 3.141.0
- Chrome Webdriver 92.0.4515.107
- IDE: PyCharm 2019.3.4

Kroki testu:
1. Test uruchamia przeglądarkę i wchodzi na adres strony https://rozklad-pkp.pl/
2. Wyszukuje połączenie kolejowe na dzień kolejny (jutrzejszy) z Krakowa do Lozanny (LAUSANNE)
3. Ze strony wyszukanych połączeń wybiera połączenie z najmniejszą liczba przesiadek
4. Wypisuje szczegóły połączenia w konsoli testu
5. Zamyka przeglądarkę


#### <b>Konfiguracja środowiska i uruchomienie projektu</b>

_1._ Pobierz i zainstaluj Python:
- https://www.python.org/downloads/
    
_2._ Pobierz i zainstaluj środowisko graficzne PyCharm ze strony:
- https://www.jetbrains.com/pycharm

Tutorial: https://www.guru99.com/how-to-install-python.html

_3._ Uruchom środowisko pierwszy raz i dodaj interpreter Python:
- https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
- https://www.jetbrains.com/help/pycharm/configuring-local-python-interpreters.html

_4._ Pobierz pliki projektu.

_5._ Pobierz przeglądarkę Chrome i odpowiadający jej wersji Webdriver:
- https://www.google.com/chrome/
- https://chromedriver.chromium.org/downloads
    
_6._ Plik chromewebdriver umieść w katalogu "tests" projektu
    
_7._ Otwórz projekt za pomocą PyCharm i w terminalu uruchom komendę:
<pre><code>pip install -r requirements.txt</code></pre>

_8._ Test można uruchomić za pomocą terminala z poziomu katalogu "test" wpisując komendę:
<pre><code>pytest -s pkpTest.py</code></pre>
