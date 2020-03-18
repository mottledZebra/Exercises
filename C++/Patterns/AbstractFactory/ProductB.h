#pragma once

#include <iostream>
using namespace std;

class ProductB
{
public:

  ProductB(void)
  {
    cout << "constructor ProductB" << endl;    
  }

  virtual ~ProductB(void)
  {
    cout << "destructor ProductB" << endl;    
  }

  virtual void runProductB() = 0;
};

