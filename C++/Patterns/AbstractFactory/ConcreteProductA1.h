#pragma once

#include <iostream>
#include "ProductA.h"

using namespace std;

class ConcreteProductA1 : public ProductA
{
public:

  ConcreteProductA1(void)
  {
    cout << "constructor ConcreteProductA1" << endl;    
  }

  virtual ~ConcreteProductA1(void)
  {
    cout << "destructor ConcreteProductA1" << endl;    
  }

  void runProductA()
  {
    cout << "ConcreteProductA1: runProductA()" << endl;
  }
};

