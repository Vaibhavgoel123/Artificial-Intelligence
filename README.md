# PyTorch
**PyTorch** is an open-source deep learning framework widely used for machine learning, AI research, and production systems. It’s known for being flexible, Python-friendly, and easy to debug.
```python
import torch
```
PyTorch is a library developed by **Meta** that provides:
1. Tensors (Similar to Numpy but with GPU support).
2. Automatic differentiation.
3. It is higly used to train **Neural Networks**.

PyTorch is easier to learn as compared to any other **Deep Learning** libraries like **Tensorflow**.
Here's a simple PyTorch program:
```python
import torch
import torch.nn as nn
import torch.optim as optim

a = torch.tensor([[1.0],[2.0],[3.0]])
b = torch.tensor([[2.0],[4.0],[6.0]])

model = nn.Linear(1,1)
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(10):
  pred = model(a)
  loss = loss_fn(pred,a)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
```
```a``` and ```b``` are tensors for defining the dataset.
In ```model``` ```nn.Linear(1,1)``` is defined this represents linear model having shape (1,1).
```loss_fn = nn.MSELoss()``` represents loss function to calculate the loss values.
```optimizer = optim.SGD(model.parameters(), lr=0.01)``` represents SGD (Stochastic Gradient Optimizer). Following is the way of its working.
For each training step:
1. Take a batch of data.
2. Compute loss
3. Compute gradient
4. Update weights
```w(new)=w(old)−η∇L(w)```

where ```∇L``` is the gradient vector.

```python
for epoch in range(10):
  pred = model(a)
  loss = loss_fn(pred,a)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
```
In this predictions were made based on the model we use, ```pred = model(a)``` for predicting values of ```a``` tensor and ```loss = loss_fn(pred,a)``` calculates the loss in making those predictions.

```optimizer.zero_grad()``` is basically used to remove previous errors for fresh calculations.

```loss.backward()``` means backpropagation to calculate errors and updates weight accordingly.

```optimizer.step()``` is the step where weights updated and machine learns.
