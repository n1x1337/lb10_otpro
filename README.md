# Лабораторная работа 10 (Prometheus Exporter)

**Выполнено доп.задание сделать в Grafana (файл grafana-dashboard.json)**

## Функционал
Экспортёр собирает и предоставляет следующие метрики:
- **Использование процессоров**:
  - Метрика: `cpu_usage` (в процентах).
- **Общая оперативная память и используемая**:
  - Метрика: `memory_total` (общая память в байтах).
  - Метрика: `memory_used` (используемая память в байтах).
- **Общий объём диска и используемый**:
  - Метрика: `disk_total` (общий диск в байтах).
  - Метрика: `disk_used` (используемый диск в байтах).

## Установка

1. Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск

1. Вы можете указать адрес и порт для запуска экспортёра с помощью переменных окружения:
```bash
EXPORTER_HOST=0.0.0.0 EXPORTER_PORT=8000 python exporter.py
```
По умолчанию экспортёр запускается на http://0.0.0.0:8000.

2. Проверка метрик
После запуска экспортёра метрики будут доступны по адресу:
```bash
http://<EXPORTER_HOST>:<EXPORTER_PORT>/metrics
```

## PromQL-запросы

Для анализа метрик в Prometheus можно использовать следующие запросы:

Использование процессоров:
```bash
cpu_usage
```

Общий объём памяти:
```bash
memory_total
```

Используемая память:
```bash
memory_used
```

Общий объём диска:
```bash
disk_total
```

Используемый объём диска:
```bash
disk_used
```
