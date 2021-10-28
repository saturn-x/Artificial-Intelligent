package tsp;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
public class Genetic {
    public double[][] map;
    public List<int[]> races;
    public List<int[]> new_races=new ArrayList<>();
    public List<int[]> pools=new ArrayList<>();
    public int sizes;
    public int cities;
    public float pm;
    public float pc;
    /*
    siezes:种群个数
    n:基因个数/城市个数
     */
    public Genetic(int sizes,int n){
        this.sizes=sizes;
        this.cities=n;
        races=new ArrayList<>(sizes);
         //置随机数种子
        Random random=new Random();
        //随机初始化种群
        for (int i = 0; i < sizes; i++) {
            //需要保证前后都为0
            int [] race=new int[n+1];

            for (int j = 1; j < n; j++) {
                int tmp=random.nextInt(cities-1)+1;
                //在每一个race都保证生成不相同的数字
                while(race[tmp]>0)//如果race[tmp]>0:证明已经被初始化过
                    tmp= random.nextInt(cities-1)+1;
                race[tmp]=j;
            }
            races.add(race);
        }
        System.out.println("初始化完成···");
    }
    public List<int[]> tourname(){
        pools.clear();
        Random random=new Random();
        for (int i = 0; i < sizes; i++) {
            int l=random.nextInt(sizes);
            int r=random.nextInt(sizes);
            if(utils.calc(races.get(l),map)<utils.calc(races.get(r),map)){
                pools.add(races.get(l));
            }else{
                pools.add(races.get(r));
            }
        }
        System.out.println("锦标赛筛选完成···");
        return pools;
    }

    public void mytoString(List<int[]> outs) {
        System.out.println("打印开始···");
        for (int[] tmp:outs
             ) {
            double length=utils.calc(tmp,map);
            for(int i :tmp){
                System.out.printf(i+" ");
            }
            System.out.println(length);
            System.out.println("");
        }
        System.out.println("打印结束···");
    }
    public int[] ret_min(){
        //返回路径最小的个体
        double min=utils.calc(races.get(0),map);
        int[] cur=races.get(0);
        for (int[] tmp:races) {
            double length=utils.calc(tmp,map);
            if(min>length){
                min=length;
                cur=tmp;
            }
        }
        return cur;
    }
    public void crossover(){
        new_races.clear();
        Random random=new Random();
        //交配算法
        while(new_races.size()<sizes){
            //两个随机数
            int one=random.nextInt(sizes);
            int[] ones=pools.get(one).clone();
            int two=random.nextInt(sizes);
            int[] twos=pools.get(two).clone();
            double cur_random=random.nextDouble();
            if(cur_random>pc){
                //获取交点
                int[] point=utils.get_2_random(cities);
                int l=point[0];int r=point[1];
                //交换两点之间的序列
                //对l->r之间的序列进行交换
                for (int i = l; i <=r-1 ; i++) {
                    int tmp=ones[i];
                    ones[i]=twos[i];
                    twos[i]=tmp;
                }
            }
            //变异
            if(cur_random>pm){
                Random rand=new Random();
                int left=rand.nextInt(cities);
                int right=rand.nextInt(cities);
                if(left > right)
                {
                    int tmp;
                    tmp=left;
                    left=right;
                    right=tmp;
                }
                //逆转left-right下标元素
                while(left < right)
                {
                    int tmp=ones[left];
                    ones[left]=ones[right];
                    ones[right]=tmp;
                    left++;
                    right--;
                }
            }
            //去重
            List<int[]> list=utils.currect(ones,twos);
            ones=list.get(0);
            twos=list.get(1);
            new_races.add(ones);
            new_races.add(twos);
        }
    }
}
