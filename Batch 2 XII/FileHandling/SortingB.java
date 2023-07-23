class SortingB {
	public static void bubbleS(int arr[]) {
		int i,j,temp,len;
		len = arr.length;
		for(i=0;i<len;i++) {
			for(j=0;j<len-1-i; j++){
				if(arr[j]>arr[j+1]) {
					temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;					
				}//closing of if
			}//closing of j				
		}//closing of i
	}
	public static void main(String args[]) {
		int A[] = new int[6];
		int i;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter any 6 elements: ");
		for(i=0;i<A.length;i++){
			A[i] = sc.nextInt();
		}
		bubbleS(A);
	}
}