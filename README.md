# gyprint
print shape for torch.Tensor

# install
`pip install gyprint`

# usage
```
import numpy as np
import torch
from gyprint import print_shape as gprint
a__int = torch.tensor([1,2,3])

lis = []
dic = dict()
lis.append(a__int)
lis.append(a__int)
listuple = tuple(lis)
dic['det'] = a__int
dic['col'] = a__int

gprint(listuple)
gprint(a__int)
gprint(dic)
'''
 ############### ['listuple'] is <class 'tuple'>, length is 2 ############### 
['listuple'], 0 =====> <class 'torch.Tensor'> =====> torch.Size([3])
['listuple'], 1 =====> <class 'torch.Tensor'> =====> torch.Size([3])
 ['a__int'] =====> <class 'torch.Tensor'> =====> torch.Size([3]) 
 ############### ['dic'] is <class 'dict'>, length is 2 ############### 
['dic'], keys: det, value=====> <class 'torch.Tensor'> =====> torch.Size([3])
['dic'], keys: col, value=====> <class 'torch.Tensor'> =====> torch.Size([3])
'''
print("done")
```

# enjoy it !!!:stuck_out_tongue_closed_eyes:
