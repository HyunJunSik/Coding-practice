import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int C=sc.nextInt();
        for(int i=0;i<C;i++){
            int st=sc.nextInt();
            int score[]=new int[st];
            double sum=0;
            double avg;
            double count=0;
            for(int j=0;j<st;j++){
                score[j]=sc.nextInt();
                sum+=score[j];
            }
            avg=sum/st;
            for(int j=0;j<st;j++){
                if(score[j]>avg){
                    count++;
                }
            }
          System.out.printf("%.3f",(count/st)*100);
            System.out.println("%");
        }
        
    }
}