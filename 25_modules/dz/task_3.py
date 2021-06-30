class Mydict(dict):

    def get(self, key):
        return_val = super().get(key)
        if return_val is None:
            return 0
        else:
            return return_val


test_dict = Mydict()

test_dict['qwert'] = 123
test_dict['asdfg'] = 234

print(test_dict.get('qwert'))
print(test_dict.get('qwerty'))
