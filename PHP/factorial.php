<?php
/*---
  С помощью рекурсии реализовать функцию вычисления факториала числа.

  Using recursion realize a function to compute the factorial of a number.
---*/
error_reporting(E_ALL);

function fact($a) {
  if($a < 0) {
    return NULL;
  }
  if($a === 0) {
    return 1;
  }
  return $a * fact($a - 1);
}

$a = rand(0, 10);
echo 'a = ' . $a . '<br>';

echo 'a! = ' . fact($a) . '<br>';
?>
