package tsp;

import java.util.Random;

public class test {
    public static void main(String[] args) {
        double[][] res=utils.init_distance(10);
        for(double[] i:res){
            for(double j:i){
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}
