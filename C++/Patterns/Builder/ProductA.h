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

  ~ProductA(void)
  {
    cout << "destructor ProductA" << endl;    
  }
};

