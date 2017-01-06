<?php
/*---
Объявить массив, в котором в качестве ключей будут использоваться названия областей,
а в качестве значений – массивы с названиями городов из соответствующей области.
Вывести города, группируя их по областям.

Declare an array, where keys will be names of regions,
and values as arrays with the names of cities from the relevant field.
Output the cities, grouping them by regions.
---*/
error_reporting(E_ALL);

$cities = [
  'Московская область' => ['Долгопрудный', 'Химки', 'Истра', 'Реутов'],
  'Ленинградская область' => ['Гатчина', 'Всеволожск', 'Кингисепп', 'Волхов'],
  'Смоленская область' => ['Смоленск', 'Вязьма', 'Рославль'],
  'Рязанская область' => ['Рязань', 'Касимов', 'Сасово']
];

foreach ($cities as $key => $value) {
  $separator = FALSE;
  echo $key . ':<br>';
  for ($i = 0; $i < count($value); $i++) {
    if ($separator) {
      echo ', ';
    }
    $separator = TRUE;
    echo $value[$i];
  }
  echo '<br>';
}
?>
