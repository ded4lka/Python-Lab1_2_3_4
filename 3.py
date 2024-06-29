import socket                   # Для получения ip
import numpy as np              # Для мат. вычислений
import matplotlib.pyplot as plt # Для диаграмм и графиков
from pythonping import ping     # Для пингования
import requests                 # Для получения HTML страницы
from bs4 import BeautifulSoup   # Для парсинга HTML кода

# 1.1
# 1.1.1
# Функция получения IP адреса по URL
def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")

# Получаем IP адрес URL
url = "www.mit.edu"
ip_address = get_ip_address(url)
if ip_address:
    print(f"The IP address of {url} is: {ip_address}")

# 1.1.2
# Функция пинга IP адреса
def pythonping_ip_address(ip_address, ping_count):
    ping_response = ping(ip_address, count=ping_count, verbose=True)
    return ping_response

# Пингуем адрес
ping_count = 1
ping_response = pythonping_ip_address(ip_address, ping_count)

# 1.1.3
# Берём и выводим кол-во отправленных и полученных пакетов
sent_amount = ping_response.stats_packets_sent
returned_amount = ping_response.stats_packets_returned
print("Sent: ", sent_amount)
print("Returned: ", returned_amount)

# 1.1.4
# Создаём массив всех 28ми времён получения пакетов
ping_times = [reply.time_elapsed for reply in ping_response._responses]

# Делаем гистограмму
counts, bin_edges = np.histogram(ping_times, bins=ping_count, density=True)

# Вычисление плотности распределения вероятности (PDF)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
pdf = counts #/ sum(counts)

# Построение графика
plt.plot(bin_centers, pdf, '-o')
plt.xlabel('Время ответа (RTT)')
plt.ylabel('PDF')
plt.title('Плотность распределения вероятности времени ответа (RTT)')
plt.grid(True)
plt.show()
    
# 1.2
# 1.2.1
# Функция парсинга почтового адреса с сайта mit.edu
def extract_postal_address(url):
    # Запрашиваем HTML код страницы
    response = requests.get(url)
    if response.status_code == 200:
        # Подключаем парсер
        soup = BeautifulSoup(response.content, 'html.parser')
        # Используем метод find_all для поиска всех элементов, содержащих информацию, которая, вероятно, содержит почтовый адрес
        potential_address_elements = soup.find_all(string=lambda text: text and (('MIT' in text or 'Massachusetts Institute of Technology' in text or '77 Massachusetts Avenue' in text) and 'USA' in text and 'MA' in text))
        if potential_address_elements:
            # Выводим первый найденный адрес
            print("Почтовый адрес MIT:")
            print(potential_address_elements)
        else:
            print("Почтовый адрес не найден.")
    else:
        print("Ошибка при получении страницы:", response.status_code)

# Парсим почтовый адрес
url = "https://www.mit.edu"
extract_postal_address(url)

# Парсинг картинки
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
img_tags = soup.find_all("img")

# Получаем базовую часть URL
base_url = url[:url.find("/", 8)]

for img_tag in img_tags:
    img_src = img_tag.get("src")
    img_url = base_url + 'u' + img_src if img_src.startswith("/") else url + "/" + img_src
    print("URL картинки:", img_url)
    break