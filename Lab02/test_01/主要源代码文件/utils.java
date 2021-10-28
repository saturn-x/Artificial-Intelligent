package tsp;

import java.util.*;

public class utils {


    //评价函数
    public static double calc(int[] race, double[][] cmap){
        float res=0;
        for(int i=0;i<race.length-1;i++){
            int l=race[i];
            int r=race[i+1];
            res+=cmap[l][r];
        }
        return res;
    }

    public static int[] get_2_random(int cities){
        Random random=new Random();
        //随机返回俩个随机数，并且确保l<r,以及r-l>=2;
        int l=0,r=0;
        while(l>=r-2||r-l==cities){
            l=random.nextInt(cities+1);
            r=random.nextInt(cities+1);
        }

        return new int[]{l,r};
    }

    //去重函数
    public static List<int[]> currect(int[] a, int[] b){
        List<int[]> list=new ArrayList<>();
        int l=find_last_repat(a);
        int r=find_last_repat(b);
        while (l!=-1||r!=-1){
            int tmp=a[l];
            a[l]=b[r];
            b[r]=tmp;
            l=find_last_repat(a);
            r=find_last_repat(b);
        }
        list.add(a);
        list.add(b);
        return list;
    }


    public static int find_last_repat(int[] tmp){
        Set<Integer> set= new HashSet<>();
        for (int i = 0; i < tmp.length-1; i++) {
            if(set.contains(tmp[i])){
                return i;
            }else{
                set.add(tmp[i]);
            }
        }
        return -1;
    }



    public static double[][]  init_distance(int cities){
        //初始化100-3000 0~10000
        Random random=new Random();
        double[][] tmp=new double[cities][cities];
        for(int i=0;i<cities;i++){
            for(int j=0;j<cities;j++){
                double cur=random.nextDouble();
                cur=500+cur*10000;
                if(i==j){
                    tmp[i][j]=0;
                }else{
                    tmp[i][j]=cur;
                }

            }
        }
        return tmp;
    }
}

