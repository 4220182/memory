# memory
我们测k8s节点根据内存的资源，驱逐POD，需要精确模拟POD占用的内存。使用下面的方法，逐渐增加POD的内存，使其达到驱逐POD。

##部署

```bash
kubectl apply -f ./deployment.yaml
```

默认，POD占用50Mi内存：
````bash
$ kubectl top pod
NAME                       CPU(cores)   MEMORY(bytes)   
memory-5c6b8d97d-rj689     1m           53Mi           
````

你可以在deployment.yaml中覆盖默认占用的内存，如设置为200Mi：
```yaml
containers:
  - name: memory
    image: koza/memory:latest
    command: ["python2","start.py","200"]
```
```bash
$ kubectl top pod
NAME                       CPU(cores)   MEMORY(bytes)   
memory-5c6b8d97d-rj689     1m           203Mi           
```

你还可以在POD启动后，进入容器，增加内存：
```bash
$ kubectl exec -it memory-5c6b8d97d-rj689 -- bash
root@memory-5c6b8d97d-rj689:/# python2 ./start.py 100

$ kubectl top pod
NAME                     CPU(cores)   MEMORY(bytes)   
memory-5c6b8d97d-rj689   1m           309Mi 
```

