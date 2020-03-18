#pragma once

#include <iostream>
#include "AbstractFactory.h"
#include "ConcreteProductA2.h"
#include "ConcreteProductB2.h"

using namespace std;

class ConcreteFactory2 : public AbstractFactory
{
public:

  ConcreteFactory2(void)
  {
    cout << "constructor ConcreteFactory2" << endl;    
  }

  virtual ~ConcreteFactory2(void)
  {
    cout << "destructor ConcreteFactory2" << endl;    
  }

  ProductA* createProductA()
  {
    cout << "ConcreteFactory2 creates ConcreteProductA2 by createProductA()" << endl;
    return new ConcreteProductA2();
  }

  ProductB* createProductB()
  {
    cout << "ConcreteFactory2 creates ConcreteProductB2 by createProductB()" << endl;
    return new ConcreteProductB2();
  }
};

