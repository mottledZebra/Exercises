#pragma once
#include "creator.h"
#include "ConcreteProductA.h"

class ConcreteCreatorA : public Creator
{
public:

  ConcreteCreatorA(void)
  {
    cout << "constructor ConcreteCreatorA" << endl;    
  }

  ~ConcreteCreatorA(void)
  {
    cout << "destructor ConcreteCreatorA" << endl;    
  }

protected:
  Product* FactoryMethod()
  {
    cout << "ConcreteCreatorA creates ConcreteProductA by FactoryMethod()" << endl;
    return new ConcreteProductA;
  }
};

