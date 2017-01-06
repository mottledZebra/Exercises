<?php
/*---
Реализовать функцию, заменяющую буквы русского алфавита символами транслитерации.

Implement a function that replaces letters of the Russian alphabet characters
to the transliteration symbols.
---*/
error_reporting(E_ALL);

function convert_translit($string) {
  $translit = [
    'А' => 'A',  'Б' => 'B',   'В' => 'V',    'Г' => 'G',  'Д' => 'D',
    'Е' => 'E',  'Ё' => 'YO',  'Ж' => 'ZH',   'З' => 'Z',  'И' => 'I',
    'Й' => 'J',  'К' => 'K',   'Л' => 'L',    'М' => 'M',  'Н' => 'N',
    'О' => 'O',  'П' => 'P',   'Р' => 'R',    'С' => 'S',  'Т' => 'T',
    'У' => 'U',  'Ф' => 'F',   'Х' => 'KH',   'Ц' => 'CZ', 'Ч' => 'CH',
    'Ш' => 'SH', 'Щ' => 'SHH', 'Ъ' => '\'\'', 'Ы' => 'Y',  'Ь' => '\'',
    'Э' => 'E',  'Ю' => 'YU',  'Я' => 'YA',
    'а' => 'a',  'б' => 'b',   'в' => 'v',    'г' => 'g',  'д' => 'd',
    'е' => 'e',  'ё' => 'yo',  'ж' => 'zh',   'з' => 'z',  'и' => 'i',
    'й' => 'j',  'к' => 'k',   'л' => 'l',    'м' => 'm',  'н' => 'n',
    'о' => 'o',  'п' => 'p',   'р' => 'r',    'с' => 's',  'т' => 't',
    'у' => 'u',  'ф' => 'f',   'х' => 'kh',   'ц' => 'cz', 'ч' => 'ch',
    'ш' => 'sh', 'щ' => 'shh', 'ъ' => '\'\'', 'ы' => 'y',  'ь' => '\'',
    'э' => 'e',  'ю' => 'yu',  'я' => 'ya'
  ];

  # разбивка многобайтной строки на символы
  $s = [];
  for ($i = 0; $i < mb_strlen($string); $i++) {
    $s[] = mb_substr($string, $i, 1);
  }

  # поиск полученных букв среди ключей таблицы транслитерации и конвертация
  $tstring = '';
  foreach ($s as $letter) {
    if (array_key_exists($letter, $translit)) {
      $tstring .= $translit[$letter];
    }
    else {
      $tstring .= $letter;
    }
  }

  return $tstring;
}
?>
