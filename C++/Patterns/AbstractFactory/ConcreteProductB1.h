#pragma once

#include <iostream>
#include "ProductB.h"

using namespace std;

class ConcreteProductB1 : public ProductB
{
public:

  ConcreteProductB1(void)
  {
    cout << "constructor ConcreteProductB1" << endl;    
  }

  virtual ~ConcreteProductB1(void)
  {
    cout << "destructor ConcreteProductB1" << endl;    
  }

  void runProductB()
  {
    cout << "ConcreteProductB1: runProductB()" << endl;
  }
};

