class SortariService:
    def interschimbari_sort(self,lista,reverse=False,key=lambda x:x):
        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if key(lista[i])>key(lista[j]):
                    aux=lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux
        if reverse==True:
            return lista[::-1]
        else:
            return lista

    def partition(self,lista,low,high,key):
        pivot=lista[high]
        i=low-1
        for j in range(low,high):
            if key(lista[j])<key(pivot):
                i=i+1
                lista[i],lista[j]=lista[j],lista[i]
        lista[i+1],lista[high]=lista[high],lista[i+1]
        return i+1
    def quick_sort_alg(self,lista,low,high,reverse,key):
        if low<high:
            partitionindex=self.partition(lista,low,high,key)
            lista=self.quick_sort_alg(lista,low,partitionindex-1,reverse,key)
            lista=self.quick_sort_alg(lista,partitionindex+1,high,reverse,key)
        if reverse==True:
            return lista[::-1]
        else:
            return lista
    def quick_sort(self,lista,reverse,key):
        return self.quick_sort_alg(lista,0,len(lista)-1,reverse,key)
    def quicksort(self,x,reverse=False,key=lambda x:x):
        if len(x)==1 or len(x)==0:
            return x
        else:
            if reverse==False:
                pivot=x[0]
                i=0
                for j in range(len(x)-1):
                    if key(x[j+1])<key(pivot):
                        x[j+1],x[i+1]=x[i+1],x[j+1]
                        i+=1
                x[0],x[i]=x[i],x[0]
                first_part=self.quicksort(x[:i],reverse,key)
                second_part=self.quicksort(x[i+1:],reverse,key)
                first_part.append(x[i])
                return first_part+second_part
            else:
                pivot=x[0]
                i=0
                for j in range(len(x)-1):
                    if key(x[j+1])>key(pivot):
                        x[j+1],x[i+1]=x[i+1],x[j+1]
                        i+=1
                x[0], x[i] = x[i], x[0]
                first_part=self.quicksort(x[:1],reverse,key)
                second_part=self.quicksort(x[i+1:],reverse,key)
                first_part.append(x[i])
                return first_part + second_part



