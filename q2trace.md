# Problem:

```
0 1 0 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

### Step-by-Step Solution:

1. **Step [1] Depth [1]:**  
   Change: $(0, 0) \rightarrow 2$

```
2 1 0 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

2. **Step [2] Depth [2]:**  
   Change: $(0, 2) \rightarrow 3$

```
2 1 3 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

3. **Step [3] Depth [3]:**  
   Change: $(0, 3) \rightarrow 4$

```
2 1 3 4 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

4. **Step [4] Depth [4]:**  
   Change: $(1, 0) \rightarrow 3$

```
2 1 3 4 
3 0 1 0 
0 4 0 3 
0 3 0 0 
```

5. **Backtracking:** $(1, 1)$

6. **Step [5] Depth [4]:**  
   Change: $(1, 0) \rightarrow 4$

```
2 1 3 4 
4 0 1 0 
0 4 0 3 
0 3 0 0 
```

7. **Backtracking:** $(1, 1)$

8. **Backtracking:** $(1, 0)$

9. **Backtracking:** $(0, 3)$

10. **Step [6] Depth [2]:**  
    Change: $(0, 2) \rightarrow 4$

```
2 1 4 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

11. **Backtracking:** $(0, 3)$

12. **Backtracking:** $(0, 2)$

13. **Step [7] Depth [1]:**  
    Change: $(0, 0) \rightarrow 3$

```
3 1 0 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

14. **Step [8] Depth [2]:**  
    Change: $(0, 2) \rightarrow 2$

```
3 1 2 0 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

15. **Step [9] Depth [3]:**  
    Change: $(0, 3) \rightarrow 4$

```
3 1 2 4 
0 0 1 0 
0 4 0 3 
0 3 0 0 
```

16. **Step [10] Depth [4]:**  
    Change: $(1, 0) \rightarrow 2$

```
3 1 2 4 
2 0 1 0 
0 4 0 3 
0 3 0 0 
```

### Solution:

```
3 1 2 4 
2 0 1 0 
0 4 0 3 
0 3 0 0 
```
