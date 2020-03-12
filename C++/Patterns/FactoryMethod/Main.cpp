#include <iostream>
#include <exception>
#include "ConcreteCreatorA.h"
#include "ConcreteCreatorB.h"

int main()
{
  Creator* creator = nullptr;
  char letter;

  cout << "Enter A or B" << endl;
  cin >> letter;

  try
  {
    if (letter == 'A' || letter == 'a')
      creator = new ConcreteCreatorA();
    else if (letter == 'B' || letter == 'b')
      creator = new ConcreteCreatorB();
    else
    {
      exception err("Wrong letter");
      throw err;
    }
  }
  catch(exception &err)
  {
    cout << err.what() << endl;
  }

  if (creator)
  {
    creator->runProduct();
  }

  delete creator;
  creator = nullptr;

  system("pause");
	return 0;
}

