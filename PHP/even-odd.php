<?php
/*---
С помощью цикла do…while написать функцию для вывода чисел от 0 до 10 с указанием их четности.

Using the do...while loop write a function to display numbers from 0 to 10 indicating their even-odd.
---*/
error_reporting(E_ALL);

$i = 0;
do {
  if (($i % 2) == 0) {
    echo $i . ' - четное число.<br>';
  }
  else if {
    echo $i . ' - нечетное число.<br>';
  }
  else if ($i == 0) {
    echo $i . ' - это ноль.<br>';
  }
  $i++;
} while ($i <= 10);
?>
