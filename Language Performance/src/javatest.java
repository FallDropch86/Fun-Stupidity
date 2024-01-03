class javatest {
    public static void main(String[] args) 
    {
        long startime = System.currentTimeMillis(); 

        int i = 0;
        while(i != 1000000000) {
            i++;
        }

        long endtime = System.currentTimeMillis();
        double timeelapsed = (endtime - startime) / 1000.0;

        System.out.println("Time taken by Java: "  + timeelapsed + " secs");
    }
}