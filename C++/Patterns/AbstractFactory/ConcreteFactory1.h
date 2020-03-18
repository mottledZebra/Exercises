#pragma once

#include <iostream>
#include "AbstractFactory.h"
#include "ConcreteProductA1.h"
#include "ConcreteProductB1.h"

using namespace std;

class ConcreteFactory1 : public AbstractFactory
{
public:

  ConcreteFactory1(void)
  {
    cout << "constructor ConcreteFactory1" << endl;    
  }

  virtual ~ConcreteFactory1(void)
  {
    cout << "destructor ConcreteFactory1" << endl;    
  }

  ProductA* createProductA()
  {
    cout << "ConcreteFactory1 creates ConcreteProductA1 by createProductA()" << endl;
    return new ConcreteProductA1();
  }

  ProductB* createProductB()
  {
    cout << "ConcreteFactory1 creates ConcreteProductB1 by createProductB()" << endl;
    return new ConcreteProductB1();
  }
};

