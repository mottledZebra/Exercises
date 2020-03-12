#pragma once

#include <iostream>
using namespace std;

class Product
{
public:

  Product(void)
  {
    cout << "constructor Product" << endl;    
  }

  virtual ~Product(void)
  {
    cout << "destructor Product" << endl;    
  }

  virtual void run() = 0;
};

