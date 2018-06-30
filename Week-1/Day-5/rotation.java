import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static int findRotationPoint(String[] words) {

        // find the rotation point in the array
        

        int start = 0;
    int end = words.length - 1;
    int result = 0;
    
    while(start < end) {
     int mid = (start + end)/2;            
            
      if(start + 1 == end) {        
        if(words[start].compareToIgnoreCase(words[end]) < 0) {          
          result = start;
        } else {
          result = end;
        }
        break;
      }
      
      if(words[mid].compareToIgnoreCase(words[start]) < 0) {
        //top half is unsorted        
        end = mid;        
      } else {
        //bottom half is unsorted
        start = mid;
      }      
    }
         
    return result;
    }
