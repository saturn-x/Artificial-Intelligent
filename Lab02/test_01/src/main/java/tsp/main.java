package tsp;

import javax.swing.*;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class main {
    public static void main(String[] args) throws IOException {

//        double[][] cmap=new double[][]{
//                {   0.   , 2538.94 , 2873.8  , 2575.27 , 2318.1  , 2158.71 , 2216.58 , 3174.04 , 3371.13 , 3540.24 },
//                {2538.94 ,    0.   , 1073.54 ,  111.288,  266.835,  395.032,  410.118,  637.942,  853.554, 1055.   },
//                {2873.8  , 1073.54 ,    0.   ,  964.495,  988.636, 1094.32 , 1382.73 , 1240.15 , 1460.25 , 1687.   },
//                {2575.27 ,  111.288,  964.495,    0.   ,  262.053,  416.707,  503.563,  624.725,  854.916, 1068.42 },
//                {2318.1  ,  266.835,  988.636,  262.053,    0.   ,  163.355,  395.14 ,  885.   , 1110.86 , 1318.19 },
//                {2158.71 ,  395.032, 1094.32 ,  416.707,  163.355,    0.   ,  338.634, 1030.34 , 1248.58 , 1447.69 },
//                {2216.58 ,  410.118, 1382.73 ,  503.563,  395.14 ,  338.634,    0.   ,  984.068, 1160.26 , 1323.7  },
//                {3174.04 ,  637.942, 1240.15 ,  624.725,  885.   , 1030.34 ,  984.068,    0.   ,  243.417,  473.768},
//                {3371.13 ,  853.554, 1460.25 ,  854.916, 1110.86 , 1248.58 , 1160.26 ,  243.417,    0.   ,  232.112},
//                {3540.24 , 1055.   , 1687.   , 1068.42 , 1318.19 , 1447.69 , 1323.7  ,  473.768,  232.112,    0.   }
//        };
        int sizes=200;//种群个数
        int cities=50;//城市个数
        float pc=0.8f;
        float pm=0.15f;
        //初始化
        double[][] ccmap=utils.init_distance(cities);
        Genetic genetic=new Genetic(sizes,cities);
        genetic.pm=pm;
        genetic.pc=pc;
        genetic.map=ccmap;
        genetic.mytoString(genetic.races);
        //选最小的个体
        List<int[]> res=new ArrayList<>();
        res.add(genetic.ret_min());
        //筛选出交配池);
        //进行变异；
        for (int i = 0; i <= 1000; i++) {
            System.out.println("执行"+i+"次");
            genetic.tourname();
            genetic.crossover();
            genetic.races=genetic.new_races;
            res.add(genetic.ret_min());
        }
        int[] res_data=new int [res.size()];
        for(int i=0;i<res.size();i++){
            res_data[i]= (int) utils.calc(res.get(i), ccmap);
            System.out.print(res_data[i]+" ");
        }

        String respath="./tmp.txt";
        FileWriter fw=new FileWriter(respath);
        for(int i=0;i<res_data.length;i++){
            fw.write(res_data[i]+"\n");
        }
        fw.flush();
        fw.close();
        String matrixpath="./matrix.txt";
        FileWriter new_fw=new FileWriter(matrixpath);
        for(double[] i:ccmap){
            for(double j:i){
                new_fw.write(j+" ");
            }
            new_fw.write("\n");
        }
        new_fw.flush();
        new_fw.close();

    }
}
