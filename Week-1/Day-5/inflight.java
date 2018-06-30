import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;


import java.util.Set;
import java.util.HashSet;

public class Solution {
  static boolean canTwoMoviesFillFlight(
    int[] movieLengths, int flightLength) {
      
    Set<Integer> seen = new HashSet<>();
    
    for (int currentMovieLength : movieLengths) {
      if (seen.contains(flightLength - currentMovieLength)) {
        return true;
      }
      seen.add(currentMovieLength);
    }
    
    return false;
  }

