#pragma once

#include <iostream>
#include "ProductB.h"

using namespace std;

class ConcreteProductB2 : public ProductB
{
public:

  ConcreteProductB2(void)
  {
    cout << "constructor ConcreteProductB2" << endl;    
  }

  virtual ~ConcreteProductB2(void)
  {
    cout << "destructor ConcreteProductB2" << endl;    
  }

  void runProductB()
  {
    cout << "ConcreteProductB2: runProductB()" << endl;
  }
};

