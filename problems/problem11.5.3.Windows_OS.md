## Windows OS

В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ "\",
затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл,
в конце пишется имя файла (C:\Windows\System32\calc.exe).

На вход программе подаётся одна строка с корректным именем файла в операционной системе Windows.
Напишите программу, которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.

**Примечание.** В Python символ <code>\ </code> обычно используется для создания специальных символьных последовательностей,
которые представляют собой управляющие символы или экранированные последовательности. Например, <code>\n</code> представляет символ новой строки,
<code>\t</code> представляет символ табуляции и т.д. Однако если символ <code>\ </code> используется как часть строки,
его следует экранировать, т.е. использовать два обратных слэша <code>\\</code>.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                | Выходные данные                                              |
|:-----------:|-----------------------------------------------|--------------------------------------------------------------|
|      1      | C:\Windows\System32\calc.exe                  | C:<br>Windows<br>System32<br>calc.exe                        |
|      2      | D:\Windows\Program Files\Beegeek\Python\1.txt | D:<br>Windows<br>Program Files<br>Beegeek<br>Python<br>1.txt |