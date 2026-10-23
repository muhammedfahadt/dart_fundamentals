class EggCounter {
  // Your code goes here.
  
  int count(int number) {
  int count = 0;
  
  while (number > 0) {
    if ((number & 1) == 1) {
      count++;
    }
    number >>= 1;
  }
  
  return count;
}

   
}