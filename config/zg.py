

def get_modules():
    return {
        'login': {
            'name': '登陆页面',
            'children': {
                'index': {'name': '用户登陆'}
            }
        },
        'fengkong_children': {
            'name': '风控模板',
            'children': {
                # 'stock': {
                #     'name': 'A股管理',
                #     'children': {
                #         'index':   {'name': '模板列表'},
                #         'create':  {'name': '新建模板'},
                #         'default': {'name': '设置默认'},
                #         'hold':    {'name': '仓比限制'},
                #         'forbid':  {'name': '禁卖股'},
                #     }
                # },
                'future': {
                    'name': '内盘期货',
                    'children': {
                        'index':    {'name': '模板列表'},
                        # 'create':   {'name': '新建模板'},
                        # 'default':  {'name': '设置默认'},
                        # 'hold':     {'name': '仓比限制'},
                        # 'sort':     {'name': '品种排序'},
                        'main':     {'name': '主力合约配置'},
                        # 'product':  {'name': '品种配置'},
                        # 'contract': {'name': '合约配置'},
                    }
                }
            }
        }
    }
