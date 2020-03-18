#pragma once

#include <iostream>

using namespace std;

class ProductA;
class ProductB;

class AbstractFactory
{
public:

  AbstractFactory(void)
  {
    cout << "constructor AbstractFactory" << endl;    
  }

  virtual ~AbstractFactory(void)
  {
    cout << "destructor AbstractFactory" << endl;    
  }

  virtual ProductA* createProductA() = 0;
  virtual ProductB* createProductB() = 0;
};

