#include <iostream>
#include <exception>
#include "ConcreteFactory1.h"
#include "ConcreteFactory2.h"

int main()
{
  AbstractFactory* factory = nullptr;
  ProductA* productA = nullptr;
  ProductB* productB = nullptr;
  char letter;

  cout << "Enter 1 or 2" << endl;
  cin >> letter;

  try
  {
    if (letter == '1')
      factory = new ConcreteFactory1();
    else if (letter == '2')
      factory = new ConcreteFactory2();
    else
    {
      exception err("Wrong letter");
      throw err;
    }
  }
  catch(exception &err)
  {
    cout << err.what() << endl;
  }

  if (factory)
  {
    productA = factory->createProductA();
    productA->runProductA();
    productB = factory->createProductB();
    productB->runProductB();
  }

  delete productA;
  productA = nullptr;
  delete productB;
  productB = nullptr;
  delete factory;
  factory = nullptr;

  system("pause");
	return 0;
}

