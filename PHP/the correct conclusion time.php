<?php
/*---
  Написать функцию, которая вычисляет текущее время и возвращает его
  в формате с правильными склонениями, например:
      22 часа 15 минут
      21 час 43 минуты
---*/
error_reporting(E_ALL);

function utime() {
  $m = (int) date('i');
  $h = (int) date('G');
  $sm = $sh = '';

  if ($h >= 2 and $h <= 4 or $h == 22 or $h == 23) {
    $sh = 'а';
  }
  else if ($h >= 5 and $h <= 20 or $h == 0) {
    $sh = 'ов';
  }
  if ($m % 10 == 1 and $m != 11) {
    $sm = 'а';
  }
  else if ($m % 10 >= 2 and $m % 10 <= 4 and ($m < 10 or $m > 20)) {
    $sm = 'ы';
  }

  return $h . ' час' . $sh . ' ' . $m . ' минут' . $sm . '<br>';
}

echo utime();
?>
