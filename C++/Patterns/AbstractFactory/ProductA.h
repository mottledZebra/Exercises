#pragma once

#include <iostream>
using namespace std;

class ProductA
{
public:

  ProductA(void)
  {
    cout << "constructor ProductA" << endl;    
  }

  virtual ~ProductA(void)
  {
    cout << "destructor ProductA" << endl;    
  }

  virtual void runProductA() = 0;
};

