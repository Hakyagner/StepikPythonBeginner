## Сбой в системе

После недавнего сбоя в операционной системе у Гвидо сбилась кодировка на компьютере.
Теперь все буквы русского алфавита отображаются в некорректном виде:

<code>[u-<номер символа в таблице Unicode>]</code>

Гвидо ещё не научился читать символы в таком формате, поэтому просит вас написать программу, которая будет "расшифровывать" для него все тексты на компьютере.

На вход программе подаётся строка текста. Расшифруйте текст, заменив все конструкции <code>[u-<номер символа в таблице Unicode>]</code>
на соответствующие буквы русского алфавита, и выведите его.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                                                                               | Выходные данные                                                |
|:-----------:|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
|      1      | Hello, my name is \[u-1061]\[u-1072]\[u-1082]\[u-1080]!                                                      | Hello, my name is Хаки!                                        |
|      2      | Username: \[u-1042]\[u-1072]\[u-1089]\[u-1103]; City: \[u-1050]\[u-1072]\[u-1079]\[u-1072]\[u-1085]\[u-1100] | Username: Вася; City: Казань                                   |
|      3      | Because I didn't know what I had until it was gone! All right?                                               | Because I didn't know what I had until it was gone! All right? |
|      4      | \[u-1093]\[u-1086]-Santa Claus-\[u-1093]\[u-1086]                                                            | хо-Santa Claus-хо                                              |
|      5      | \[u-1057]\[u-1058]\[u-1045]\[u-1055]\[u-1048]\[u-1050]                                                       | СТЕПИК                                                         |