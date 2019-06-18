def list_change(list1,list2,operation):
	i=0
	multiplication=0
	while i<len(list1):
		if operation == "multiplication":    	
			b=0
			sum=0
			while b<list1[i]:
				sum=sum+list2[i]
				b=b+1
			print sum
		i=i+1
list_change([5, 10, 50, 20], [2, 20, 3, 5],"multiplication")

