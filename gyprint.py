
import numpy as np
import torch
import  sys
import inspect

__all__ = ['print_shape',]

class GY_DEFINE_COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_shape(_args : None, 
        segfix : str ="=====>",
        show_value: bool = False) -> None:
    # one dim tensor only into consideration, Currently !!!
    # only used print one's shape !!
    # if you have any question...
    assert _args is not None, f"please promise gyprint.print_shape Tensor is not None, {print_shape.__annotations__}" 
    assert type(segfix) is str, f"please promise gyprint.print_shape segfix is str, {print_shape.__annotations__}"
    def __retrieve_name(__var) -> None:
        assert __var is not None, "please promise __var is not None"
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is __var]
    __tensor_name = __retrieve_name(_args)
    def __print_tensor_shape(_tensor,index = None,keys = None,colors = None):
        if keys is not None:
            print(f'{__tensor_name}, keys: {keys}, value{segfix} {type(_tensor)} {segfix} {_tensor.shape}')
        elif index is not None:
            print(f'{__tensor_name}, {index} {segfix} {type(_tensor)} {segfix} {_tensor.shape}')
        else:
            print(GY_DEFINE_COLORS.BOLD,f'{__tensor_name} {segfix} {type(_tensor)} {segfix} {_tensor.shape}',GY_DEFINE_COLORS.ENDC)
    
    if type(_args) == torch.Tensor or type(_args) == np.ndarray:
        # format : tensor_name ===> tensor_type ===> tensor_shape
        __print_tensor_shape(_args)
        
    elif isinstance(_args,(list,tuple)):
        print(GY_DEFINE_COLORS.OKGREEN,'#'*15,f'{__tensor_name} is {type(_args)}, length is {len(_args)}','#'*15,GY_DEFINE_COLORS.ENDC)
        # _args = _args if type(_args) == list else list(_args)
        for index, item in enumerate(_args):
            if isinstance(item, (torch.Tensor,np.ndarray)):
                __print_tensor_shape(item, index=index)
            else:
                pass
    elif isinstance(_args,dict):
        # then print key:value, method type, else no implementation
        print(GY_DEFINE_COLORS.OKBLUE,'#'*15,f'{__tensor_name} is {type(_args)}, length is {len(_args)}','#'*15,GY_DEFINE_COLORS.ENDC)
        for keys, value in _args.items():
            assert isinstance(value,(torch.Tensor,np.ndarray)), f"please promise the value of {__tensor_name} is torch.Tensor or numpy"
            __print_tensor_shape(value,keys=keys)
    else:
        raise NotImplementedError
    print(_args) if show_value else None
        
        
