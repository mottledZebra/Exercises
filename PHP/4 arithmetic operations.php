<?php
/*---
  Реализовать основные 4 арифметические операции в виде функций с двумя параметрами.
  Реализовать функцию с тремя параметрами: function mathOperation($arg1, $arg2, $operation),
  где $arg1, $arg2 – значения аргументов, $operation – строка с названием операции.
  В зависимости от переданного значения операции выполнить одну из арифметических операций.

  Realize the 4 major arithmetic operations as functions with two parameters.
  Realize the function with three parameters: function mathOperation($arg1, $arg2, $operation),
  where $arg1, $arg2 – argument values, $operation – a string with the name of the operation.
  Depending on the transferred value of operation execute an arithmetic operation.
---*/
error_reporting(E_ALL);

function sum($a, $b) {
  return $a + $b;
}

function sub($a, $b) {
  return $a - $b;
}

function div($a, $b) {
  if ((int) $b === 0) {
    return NULL;
  }
  return $a / $b;
}

function mul($a, $b) {
  return $a * $b;
}

function mathOperation($arg1, $arg2, $operation){
  switch ($operation) {
    case 'sum':
      return sum($arg1, $arg2);
      break;
    case 'sub':
      return sub($arg1, $arg2);
      break;
    case 'div':
      return div($arg1, $arg2);
      break;
    case 'mul':
      return mul($arg1, $arg2);
      break;
    default:
      return NULL;
      break;
  }
}

$a = rand(-10, 10);
$b = rand(-10, 10);

echo 'a = ' . $a . '<br>';
echo 'b = ' . $b . '<br>';

echo 'a + b = ' . mathOperation($a, $b, 'sum') . '<br>';
echo 'a - b = ' . mathOperation($a, $b, 'sub') . '<br>';
echo 'a / b = ' . mathOperation($a, $b, 'div') . '<br>';
echo 'a * b = ' . mathOperation($a, $b, 'mul') . '<br>';
?>
