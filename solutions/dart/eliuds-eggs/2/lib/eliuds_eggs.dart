class EggCounter {
  // Your code goes here.
  
  int count(int number) {
  int count = 0;
  
  while (number > 0) {

    number &= (number - 1);
    count++;
  }
  return count;
   
}
}