<?php
/*---
	Объявить две целочисленные переменные $a и $b и задать им
	произвольные начальные значения. Затем написать скрипт,
	который работает по следующему принципу:
		a.	если $a и $b положительные, вывести их разность;
		b.	если $а и $b отрицательные, вывести их произведение;
		c.	если $а и $b разных знаков, вывести их сумму;
	ноль можно считать положительным числом.

	Declare two integer variables, $a and $b and set them
	to arbitrary initial values. Then write a script
	that works on the following principle:
		a. if $a and $b are positive, output their difference;
		b. if $a and $b is negative, output their multiplication;
		c. if $a and $b are of different signs, output their sum;
	zero can be considered positive.
---*/

error_reporting(E_ALL);

$a = rand(-10, 10);
$b = rand(-10, 10);

echo 'a = ' . $a . '<br>';
echo 'b = ' . $b . '<br>';

if ($a >= 0 and $b >= 0) {
  echo 'a - b = ' . ($a - $b);
}
else if ($a < 0 and $b < 0) {
  echo 'a * b = ' . ($a * $b);
}
else {
  echo 'a + b = ' . ($a + $b);
}

?>
