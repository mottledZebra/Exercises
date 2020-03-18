#pragma once

#include <iostream>
#include "ProductA.h"

using namespace std;

class ConcreteProductA2 : public ProductA
{
public:

  ConcreteProductA2(void)
  {
    cout << "constructor ConcreteProductA2" << endl;    
  }

  virtual ~ConcreteProductA2(void)
  {
    cout << "destructor ConcreteProductA2" << endl;    
  }

  void runProductA()
  {
    cout << "ConcreteProductA2: runProductA()" << endl;
  }
};

