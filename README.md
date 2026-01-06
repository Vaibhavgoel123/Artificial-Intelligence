# PyTorch Tensor
A PyTorch Tensor is a core data structure in PyTorch. It is similar to Numpy but with GPU support and automatic differentiation designed specifically for **Deep Learning**.
```python
import torch
```
Example:
```python
t = torch.tensor([[1],[2],[3]])
```
PyTorch fundamentals involves Tensors as well.
Numpy arrays can be converted to PyTorch tensors with the help of the following:
```python
import numpy as np
arr = np.array([1,2,3])
t = torch.from_numpy(arr)
```
Some of its basic operations are:
```python
t.shape
t.dtype
t.device
```
Its datatypes involves:
```
1. int8 -> Memory management
2. int64 -> Highly efficient
3. float32 -> Highly used
4. float64 -> Enhanced precision
```
Tensors can be reshpaed using ```squeeze() and unsqueeze()``` method:
```python
#Sample Data
single_distance = torch.tensor(25.0)
#Adding one dimension
with_dist = single_distance.unsqueeze(0)
#Model ready dim
ready = with_dist.unsqueeze(1)

ready.shape

squeezed = ready.squeeze()
squeezed.shape
squeezed
```
Output:
```
torch.Size([1, 1])
torch.Size([])
tensor(25.)
```
Tensor Maths
```python
distances = torch.tensor([[3.0],[7.0],[12.0]])
weight = 2.3
bias = 8.0
distances*weight+bias
```
Output:
```
tensor([[14.9000],
        [24.1000],
        [35.6000]])
```
Calculating weights involves multiple operations and matrix multiplication or scalar multiplication is one of them.

Multiplying small matrix is fine but when talking about large matrix to multiply single array to large matrix we need to create a matrix of that same size of the elements of that array so it increases the complexity.

To overcome this **Broadcasting** method was introduced. Broadcasting means to repeat the values to match the dimensions of the corresponding matrix.

**PyTorch** automatically expands the dimensions in the case of scaler operations so in broadcasting the Pytorch compares the dimensions of both entities and try to match them, if anyone entity matches perfectly then it try to match the other one by repeating the values.
