#coding:utf-8

ss = '&#xe0e0,&#xe867'
def decyrpt_text(res):
    mapping=\
        {'&#xe0e0': '0', '&#xf60f': '1', '&#xe04b': '2', '&#xea54': '3', \
         '&#xe867': '4', '&#xe6b1': '5','&#xe5d1': '6', '&#xf805': '7',\
         '&#xf5df': '8', '&#xea9e': '9'
         }

    for key,value in mapping.items():

        html = res.replace(key,value)
    return html

if __name__ == '__main__':
    decyrpt_text(ss)