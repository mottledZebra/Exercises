#include <iostream>
#include <exception>
#include "Director.h"
#include "ConcreteBuilderA.h"
#include "ConcreteBuilderB.h"

int main()
{
  Director* director = nullptr;
  ConcreteBuilderA* builderA = nullptr;
  ConcreteBuilderB* builderB = nullptr;
  ProductA* productA = nullptr;
  ProductB* productB = nullptr;
  char letter;

  cout << "Enter 1 or 2" << endl;
  cin >> letter;

  try
  {
    if (letter == '1')
    {
      director = new Director();

      builderA = new ConcreteBuilderA();
      director->makeConstruction1(builderA);
      productA = builderA->getResult();

      builderB = new ConcreteBuilderB();
      director->makeConstruction1(builderB);
      productB = builderB->getResult();
    }
    else if (letter == '2')
    {
      director = new Director();

      builderA = new ConcreteBuilderA();
      director->makeConstruction2(builderA);
      productA = builderA->getResult();

      builderB = new ConcreteBuilderB();
      director->makeConstruction2(builderB);
      productB = builderB->getResult();
    }
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

  delete productA;
  productA = nullptr;
  delete productB;
  productB = nullptr;
  delete builderA;
  builderA = nullptr;
  delete builderB;
  builderB = nullptr;
  delete director;
  director = nullptr;

  system("pause");
	return 0;
}

