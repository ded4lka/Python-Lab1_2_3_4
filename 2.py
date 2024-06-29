from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import time as timer

# Старт таймера
start_time = timer.time()

# Загрузка звукового файла
sample_rate, data = wavfile.read("2/18.wav")
print("Частота дискретизации: ", sample_rate)

# Извлечение одного канала (если файл содержит стерео)
if len(data.shape) > 1:
    data = data[:, 0]

# 1.1
# Круговая диаграмма
num_samples = len(data[:100])                                       # Кол-во семплов
theta = np.linspace(0, 4 * np.pi, num_samples, endpoint=False)      # Вычисление теты (для полярных координат)
r = np.abs(data[:100])                                                    # Амплитуды лучей

# Построение круговой диаграммы
# plt.figure(figsize=(5, 5))                  # Окно диаграммы
# ax = plt.subplot(111, projection='polar')   # Полярная система координат
# ax.plot(theta, r)                           # Зависимость
# ax.set_rmax(np.max(r))                      # Ограничение максимальной
# ax.set_rticks([])  # Убираем деления на радиусе
# plt.title('Pie chart')
# plt.show()

# Pie chart
first_100_samples = data[:100]
first_100_samples = np.abs(first_100_samples)
plt.figure(figsize=(6, 6))
plt.pie(first_100_samples, labels=[f"Sample {i}" if (i) % 5 == 0 else '' for i in range(1, len(first_100_samples) + 1)])
plt.title('Круговая диаграмма для первых 100 отсчётов')
plt.show()

# 1.2
# Вычисление временной шкалы
duration = len(data[:100]) / sample_rate
time = np.linspace(0., duration, len(data[:100]))

# Построение осциллограммы
plt.figure(figsize=(10, 4))             # Окно графика
plt.plot(time, data[:100], color='b')         # Зависимость
plt.xlabel('Time (s)')                  # OX - время   
plt.ylabel('Amplitude')                 # OY - амплитуда
plt.title('Waveform of Sound Signal')   # Наименование графика
plt.grid(True)                          # Сетка
plt.show()

#1.3
# Вычисление ДПФ (дискретное преобразование Фурье)
fft_result = np.fft.fft(data[:100])

# Вычисление амплитуды спектра
magnitude_spectrum = np.abs(fft_result)

# Преобразование амплитуды спектра к логарифмической шкале
log_magnitude_spectrum = np.log1p(magnitude_spectrum**2)  # Используем log1p для стабильности при нулевых значениях

# Вычисление частот
frequencies = np.fft.fftfreq(len(data[:100]), 1/sample_rate)

# Построение графика
plt.figure(figsize=(10, 4))                                     # Окно графика
plt.plot(frequencies[:len(frequencies)//2], \
    log_magnitude_spectrum[:len(frequencies)//2], color='b')    # Зависимость
plt.xlabel('Frequency (Hz)')    # OX - Частота
plt.ylabel('Log Magnitude')     # OY - порядок величины
plt.title('Spectral Analysis')  # Наименование графика
plt.grid(True)                  # Сетка
plt.show()

# Время выполнения программы
print (timer.time() - start_time, "seconds")