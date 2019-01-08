import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
torch.optim as optim

dataframe = pd.read_csv('./irisdata.csv')

two_class = dataframe[dataframe['species'] != 'setosa']

two_class.loc[two_class['species'] == 'virginica', 'species'] = 0
two_class.loc[two_class['species'] == 'virginica', 'species'] = 1

in_vec = two_class[['petal_length', 'petal_width']]
out_vec = two_class['species']

plt.scatter(in_vec.values[:,0], in_vec.values[:,1], c=out_vec.values)
plt.colorbar()
plt.show()


num_in = 2 # size of input attributes
num_out = 1 # size of output

class Network(nn.Module):
	def __init__(self):
		super(Network, self).__init__()
		self.fullyconnected1 = nn.Linear(nums_in, nums_out)

	def forward(self, x):
	x = self.fullyconnected1(x)
	x = F.sigmoid(x)
	return x

model = Network()
criterion == nn.MSELoss() # loss function
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01) # try tuning the learning rate


num_epochs = 1000 #number of training iterations
num_examples = two_class.shape[0]

model.train()

for epoch in range(num_epochs):
	for idx in range(num_examples):

		# for examples 'idx', convert data to tensors so that PyTorch can use it
		attributes = torch.tensor(in_vec.iloc[idx].values, dtype = torch.float)
		label = torch.tensor(out_vec.iloc[idx], dtype = torch.float)

		optimizer.zero_grad()

		output = model(attributes)

		loss = criterion(output, label)

		loss.backward()

		optimizer.step()

	if(epoch % 100 == 0):
		print('Epoch: {} | Loss : {: .6f}'.format(epoch, loss.item()))


model.eval()

pred = torch.zeros(out_vec.shape)

for idx in range(num_examples):
	attributes = torch.tensor(in_vec.iloc[idx].values, dtype=torch.float)
	label = torch.tensor(out_vec.iloc[idx], dtype=torch.float)

	pred[idx] = model(attributes).round()

print('Correct classifications: {}/{}'.format(sum(pred == torch.ensor(out_vec.values))))