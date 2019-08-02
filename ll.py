
# import torch
# import torch.nn.functional as F
# import torch.nn as nn
# # input is of size N x C = 3 x 5
# m = nn.LogSoftmax(dim=1)
# input = torch.randn(3, 5, requires_grad=True)
# print(input)
# print(F.softmax(input))
# print(F.log_softmax(input))
# print(m(input))
# # each element in target has to have 0 <= value < C
# target = torch.tensor([1, 0, 4])
# output = F.nll_loss(m(input), target)
# print(output)
# print(output.backward())

# import string
#
# def remove_punc(text):
#     exclude = set(string.punctuation)
#     return ''.join(ch for ch in text if ch not in exclude)
# def white_space_fix(text):
#     return ' '.join(text.split())
# b=remove_punc('I LOVE the Beijing!')
# a=white_space_fix(b)
# print(a)

# from collections import Counter
#
# a=Counter(['a','abc','bca','js','a','b','b'])
# b=Counter(['c','ccc','aa','a'])
# c=a&b
# print(c)

# prediction='abc'
# ground_truths=['abc','aa']
# b=(float(bool(prediction) == bool(ground_truths)))
# print(b)


import torch
a=torch.randn(3,5)
print(a)
max_in_row,_=torch.max(a,dim=1)
max_in_col,_=torch.max(a,dim=0)
print(max_in_row,max_in_col)
start_idxs=torch.argmax(max_in_row,-1)
end_idxs=torch.argmax(max_in_col,-1)
print(start_idxs,end_idxs)