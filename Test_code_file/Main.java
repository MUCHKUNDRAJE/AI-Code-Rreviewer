
class Main {
    public static void main (String arg[])
   {
   int  N = 4;
   int [] arr = {1,2,2,3} ;
   int x = 2; 
   
   int start = 0 ;
   int end = arr.length-1;


   while ( start < end) {
     int mid = start +(end-start)/2;
     
     if (arr[mid] < x) start = mid+1;

     else end=mid+1;

}

  System.out.println(start);

   }   
}