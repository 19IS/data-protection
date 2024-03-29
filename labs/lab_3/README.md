# Лабораторная работа №3 `Шифр Вижинера`

## Теория

В случае моноалфавитных подстановок используется только один алфавит шифрования. Существуют шифры, где используется целый набор алфавитов шифрования. Такие шифры называются полиалфавитными и позволяют, в отличие от моноалфавитных подстановок, скрыть естественную частоту появления символов в тексте.

**Простая полиалфавитная подстановка (или шифр Вижинера)** последовательно и циклически меняет используемые алфавиты шифрования. Число используемых алфавитов называется периодом шифра. Для шифрования используется ключ – слово или бессмысленный набор символов нормативного алфавита. Каждая буква ключа определяет свой алфавит шифрования, который получается из нормативного циклического сдвига на количество символов, равное числовому эквиваленту буквы ключа. Очевидно, что длина ключа равна периоду шифра.

Алгоритм шифрования сообщение шифром Вижинера состоит из следующих этапов:

- Под каждой буквой открытого текста помещается буква ключа
- Ключ циклически повторяется необходимое число раз
- Вычисляют числовой эквивалент буквы шифртекста, числовой эквивалент буквы ключа складывается по модулю `L` с числовым эквивалентом буквы открытого текста, где `L` – мощность нормативного алфавита. То есть шифр Вижинера описывается следующим выражением:
`Ei = ( Mi + Ki(mod U) ) mod L`, где `Ei`, `Mi` – числовые эквиваленты символов криптограммы и открытого текста соответственно, `Ki` (`mod U`) – числовой эквивалент буквы ключа, `L` – мощность нормативного алфавита, `U` – длина ключа или период шифра.
- Буквы ключа определяют величину смещения символов криптограммы относительно символов открытого текста.

## Задание

Реализовать программно алгоритм шифрования Вижинера степени n, среда разработки и язык программирования используется на усмотрение студента. При выполнении лабораторной работы необходимо предусмотреть выдачу на экран: ключа исходного, шифрованного и расшифрованного текстов.

### Вариант 5

- Сообщение: Информация становится знанием, когда она переработана и проанализирована человеком.
- Ключ: требования

### Запуск скрипта

```shell
python labs/lab_3/lab_3.py
```

## Примеры работы скрипта

![image](https://user-images.githubusercontent.com/60512214/191979736-882ffda6-906b-4187-a5f0-7f98ff34afd9.png)
