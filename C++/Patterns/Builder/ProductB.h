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

  ~ProductB(void)
  {
    cout << "destructor ProductB" << endl;    
  }
};

