<?php
/*---
С помощью цикла while вывести все числа в промежутке от 0 до 100, которые делятся на 3 без остатка.

Using a While loop display all numbers in the interval from 0 to 100 that are divisible by 3 without a remainder.
---*/
error_reporting(E_ALL);

$i = 0;
while ($i <= 100) {
  if (($i % 3) == 0) {
    echo $i . '<br>';
  }
  $i++;
}
?>
