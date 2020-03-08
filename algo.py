# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:13:57 2020

@author: bruceye
"""

import numpy as np
from itertools import combinations as cbn
from itertools import product as prd
from tqdm import trange
from tools import ParaArray


def calc_core(para):
    """伤害计算核心部分"""
    atk = para['atk']
    crit = para['crit']
    crit_dam = para['crit_dam']
    combo = para['combo']
    combo_dam = para['combo_dam']
    scaling = para['scaling']
    anger_rate = para['anger_rate']
    conti_begin = para['conti_begin']
    conti_delta = para['conti_delta']
    skill_rate = para['skill_rate']
    hits = para['hits']
    dfc_rate = para['dfc_rate']
    dfc_rate_crit = para['dfc_rate_crit']

    rtn_normal = (1 - crit) * dfc_rate + crit * crit_dam * dfc_rate_crit
    rtn_combo = combo_dam * combo
    rtn_other = [skill_rate[i] * rtn_normal + hits[i] * rtn_combo for i in range(3)]

    rtn_ub = (1 + crit * (crit_dam - 1) + 4 * rtn_combo) * dfc_rate
    rtn_ub *= skill_rate[-1] * anger_rate
    rtn_other.append(rtn_ub)

    rtn = sum(rtn_other[i] * (conti_begin + conti_delta[i]) for i in range(4))
    rtn *= atk * (1 + scaling)

    return rtn


class MFQ:
    def __init__(self, mfq_choice, mfq_k, mfq_num, atk_base):

        self.mfq_attr_main = {  # 魔法器主词条属性表
            'atk': 125,  # 攻击
            'atk_bonus': 0.1,  # 基础攻击
            'crit': 0.12,  # 暴击率
            'combo': 0.12,  # 连击率
            'scaling': 0.08,  # 伤害加成
        }
        self.mfq_attr_minor = {  # 魔法器随机词条属性表
            'atk': 125,  # 攻击
            'atk_bonus': 0.1,  # 基础攻击
            'crit': 0.12,  # 暴击率
            'crit_dam': 0.2,  # 暴击伤害
            'combo': 0.12,  # 连击率
            'combo_dam': 0.02,  # 连击伤害
            'scaling': 0.08,  # 伤害加成
        }
        self.mfq_name_map = {
            'atk': '攻击',
            'atk_bonus': '基础攻击',
            'crit': '暴击率',
            'crit_dam': '暴击伤害',
            'combo': '连击率',
            'combo_dam': '连击伤害',
            'scaling': '伤害加成',
        }
        self.mfq_key_main = list(self.mfq_attr_main)
        self.mfq_key_minor = list(self.mfq_attr_minor)
        self.mfq_filter_list = [
            {'atk_bonus': 1, 'crit': 2},  # 阴之水晶球
            {'atk_bonus': 1, 'combo': 2},  # 不蚀的箭矢
            {'combo': 1, 'scaling': 1, 'crit': 1},  # 六面回音骰
            {'crit': 1, 'scaling': 1, 'combo': 1},  # 女王的金器
            {'crit': 1, 'atk': 1, 'combo': 1},  # 倒流的沙漏
            {'atk': 1},  # 银质假面
            {'scaling': 1, 'atk_bonus': 1},  # 石封之光
            {'combo': 1, 'crit': 1},  # 指引的胸针
            {'atk': 1},  # 龙纹手杖
            {'atk': 1},  # 附灵之戒
            {'atk_bonus': 1},  # 颤栗之匙
            {},  # 魔焰匕首
            {},  # 命运之刻
            {},  # 古怪的陶罐
            {'atk_bonus': 1, 'atk': 1},  # 沉睡的吊坠
        ]

        if mfq_choice >= 0:
            self.mfq_main_num_limit = min(sum(self.mfq_filter_list[mfq_choice].values()) + 1, 3)
            self.mfq_filter = self.mfq_filter_gen(mfq_choice)
            for key in self.mfq_attr_minor:
                self.mfq_attr_minor[key] *= mfq_k
            mfq_main, mfq_minor = self.get_mfq_arr(mfq_num, atk_base)
        else:
            mfq_main, mfq_minor = [[0] * len(self.mfq_attr_main)], [[0] * len(self.mfq_attr_minor)]

        self.mfq_arr = self.merge_mfq_arr(mfq_main, mfq_minor)

    def get_mfq_idx_main(self, x):
        return self.mfq_key_main.index(x)

    def get_mfq_idx_minor(self, x):
        return self.mfq_key_minor.index(x)

    def get_mfq_idx_offset(self, x):
        return len(self.mfq_attr_main) + self.mfq_key_minor.index(x)

    def mfq_filter_gen(self, idx):
        """魔法器主属性筛选函数生成"""
        temp = self.mfq_filter_list[idx]
        return lambda cnt: sum(min(temp[key], cnt[self.get_mfq_idx_main(key)]) for key in temp) >= sum(cnt) - 1

    def get_mfq_arr(self, mfq_num, atk_base):
        """获取魔法器范围"""

        def get_mfq_cnt(mfq_attr, _mfq_num):
            n = len(mfq_attr)
            mfq_cnt = [0] * n
            idx = 0
            while idx < n:
                if sum(mfq_cnt) == _mfq_num:
                    yield mfq_cnt.copy()
                idx = 0
                while idx < n:
                    mfq_cnt[idx] += 1
                    if mfq_cnt[idx] <= 3:
                        break
                    mfq_cnt[idx] -= 4
                    idx += 1

        atk1 = self.get_mfq_idx_minor('atk')
        atk2 = self.get_mfq_idx_minor('atk_bonus')
        if self.mfq_attr_minor['atk'] < self.mfq_attr_minor['atk_bonus'] * atk_base:
            atk1, atk2 = atk2, atk1

        def mfq_atk_filter(x):
            return x[atk1] == 3 or x[atk2] == 0

        mfq_main = get_mfq_cnt(self.mfq_attr_main, self.mfq_main_num_limit)
        mfq_main = filter(self.mfq_filter, mfq_main)
        mfq_minor = get_mfq_cnt(self.mfq_attr_minor, mfq_num)
        mfq_minor = filter(mfq_atk_filter, mfq_minor)

        return mfq_main, mfq_minor

    @staticmethod
    def merge_mfq_arr(mfq_main, mfq_minor):
        mfq_merge = [main + minor for main, minor in prd(mfq_main, mfq_minor)]
        mfq_merge = np.array(mfq_merge, dtype="uint32").transpose()
        mfq_merge = np.unique(mfq_merge, axis=1)
        return mfq_merge

    def mfq_print(self, cnt):
        name = [self.mfq_name_map[x] for x in self.mfq_attr_main]
        name += [self.mfq_name_map[x] for x in self.mfq_attr_minor]
        s = {'主词条': {}, '随机词条': {}}
        for i in range(5):
            if cnt[i] > 0:
                s['主词条'][name[i]] = cnt[i]
        for i in range(5, len(cnt)):
            if cnt[i] > 0:
                s['随机词条'][name[i]] = cnt[i]
        return s


class Solver:
    def __init__(self):
        self.para = {}
        self.skill_info = self.panel_info = self.para_info = None
        self.mfq = self.mfq_info = self.mfq_choice = None
        self.xzq_info = None
        self.para_limit = self.xzq_limit = None

    def load_role(self, file_path):
        self.skill_info = ParaArray(file_path, 'skill')
        self.panel_info = ParaArray(file_path, 'panel')
        self.para_info = ParaArray(file_path, 'base_para')
        self.para_limit = ParaArray(file_path, 'paralimit')
        self.xzq_limit = ParaArray(file_path, 'xzqlimit')

    def load_mfq(self, file_path, mfq_choice, mfq_k, mfq_num):
        atk_base = self.para_info.value("atk_base", "值")
        mfq = MFQ(mfq_choice, mfq_k, mfq_num, atk_base)

        mfq_info = ParaArray(file_path, 'mfq')
        if mfq_choice == 0:  # 阴之水晶球
            self.para['dfc_ign_crit'] = 0.4
            self.para['arrow'] = 0
        elif mfq_choice == 1:  # 不蚀的箭矢
            self.para['dfc_ign_crit'] = 0
            self.para['arrow'] = 1
        elif mfq_choice >= 2:  # 其他魔法器
            self.para['dfc_ign_crit'] = 0
            self.para['arrow'] = 0
        else:  # 不重塑魔法器
            self.para['dfc_ign_crit'] = mfq_info.value('dfc_ign_crit', 0)
            self.para['arrow'] = mfq_info.value('arrow', 0)

        mfq_row_name = set(mfq.mfq_attr_minor.keys())
        mfq_row_name |= set(mfq_info.row_index.keys())
        mfq_info.row_extend([x for x in mfq_row_name if x not in ('dfc_ign_crit', 'arrow')])

        if mfq_choice >= 0:
            mfq_info.col_extend(range(mfq.mfq_arr.shape[1]))
            mfq_info.data *= 0
            for x in mfq.mfq_key_main:
                a = mfq.mfq_attr_main[x]
                b = mfq.mfq_arr[mfq.get_mfq_idx_main(x)]
                mfq_info.data[mfq_info.row_index[x]] += a * b
            for x in mfq.mfq_key_minor:
                a = mfq.mfq_attr_minor[x]
                b = mfq.mfq_arr[mfq.get_mfq_idx_offset(x)]
                mfq_info.data[mfq_info.row_index[x]] += a * b

        for x in self.panel_info.row_index:
            if x in mfq_info.row_index:
                mfq_info.data[mfq_info.row_index[x]] += self.panel_info.value(x, '值')

        self.mfq = mfq
        self.mfq_info = mfq_info
        self.mfq_choice = mfq_choice

    def load_xzq(self, file_path):
        xzq_info = ParaArray(file_path, '心之器属性')
        xzq_lv = ParaArray(file_path, '心之器等级')
        self.xzq_adjusting(xzq_info, xzq_lv)
        self.xzq_info = xzq_info

    @staticmethod
    def xzq_adjusting(xzq_info, xzq_lv):
        xzq_name = set(xzq_info.row_index.keys())
        xzq_name &= set(xzq_lv.row_index.keys())
        xzq_name = [xzq for xzq in xzq_name if xzq_lv.value(xzq, '突破数') >= 0]
        xzq_info.row_extend(xzq_name)
        xzq_lv.row_extend(xzq_name)

        atk = xzq_info.get_col('atk')
        lv = xzq_lv.get_col('等级')
        brk = xzq_lv.get_col('突破数')

        atk_begin = atk * 66 / 366
        atk = atk_begin + (atk - atk_begin) * (lv - 1) / 49

        xzq_info.transpose()
        xzq_info.data *= 0.5 + brk * 0.1
        xzq_info.data[xzq_info.row_index['atk']] = atk
        xzq_info.transpose()

    def calc_xzq(self, result_num, xzq_choice: set):
        def valid_xzq(xzq, y):
            """心之器阈值判定"""
            return sum(self.xzq_info.value(x, y) for x in xzq) * 1.0001

        para_limit = {}
        for key in self.para_limit.row_index:
            if key not in self.mfq_info.row_index:
                print("There is no such property:", key)
            v = self.para_limit.value(key, '值')
            if v > 0:
                para_limit[key] = v

        xzq_arr = cbn(self.xzq_info.row_index.keys(), 3)
        if xzq_choice:
            xzq_arr = filter(lambda xzq: xzq_choice.issubset(xzq), xzq_arr)
        vampire = self.xzq_limit.value('vampire', '值')
        if vampire > 0:
            xzq_arr = filter(lambda xzq: valid_xzq(xzq, 'vampire') > vampire, xzq_arr)

        n21 = self.xzq_limit.value('n2', '值')
        n22 = self.xzq_limit.value('n4', '值')
        s1 = '战斗开始时获得怒气'
        s2 = '每回合获得怒气'
        s3 = '战斗怒气提高'
        if n21 - n22 > 0:
            xzq_arr = filter(lambda xzq: (valid_xzq(xzq, s2) + n22) * (1 + valid_xzq(xzq, s3)) > n21, xzq_arr)
        n11 = self.xzq_limit.value('n1', '值')
        n12 = self.xzq_limit.value('n3', '值')
        if n11 - n12 > 0:
            xzq_arr = filter(
                lambda xzq: valid_xzq(xzq, s1) + (valid_xzq(xzq, s2) + n22 + n12) * (1 + valid_xzq(xzq, s3)) > n11,
                xzq_arr)

        xzq_arr = list(xzq_arr)
        if len(xzq_arr) == 0:
            return []
        xzq_ind = np.array([[self.xzq_info.row_index[x] for x in xzq] for xzq in xzq_arr], dtype="uint32")
        xzq_ind = xzq_ind.transpose()
        xzq_val = sum(self.xzq_info.data[x] for x in xzq_ind)
        xzq_val = xzq_val.transpose()

        atk_base = self.para_info.value("atk_base", "值")
        combo_to_crit = self.para_info.value("combo_to_crit", "值")

        self.skill_info.data = np.maximum(self.skill_info.data, 0)
        ratio = self.skill_info.get_row('ratio')
        hits = self.skill_info.get_row('hits')
        skill = self.skill_info.get_row('skill')
        hits = [max(x, 1) for x in hits]

        skill_scaling = [0] + [xzq_val[self.xzq_info.col_index[x]] for x in ['ap', 'sp', 'ub']]
        self.para['skill_rate'] = [((1 + skill_scaling[i]) * skill[i] * ratio[i]) for i in range(4)]
        self.para['hits'] = [x * y for x, y in zip(hits, skill)]

        self.para['conti_begin'] = self.para_info.value('conti_begin', '值')
        if 'conti_real' in self.skill_info.row_index:
            conti_real = self.skill_info.get_row('conti_real')
            conti_delta = [conti_real[i] for i in range(4)]
        else:
            conti = self.skill_info.get_row('conti')
            conti_delta = [conti[i] / hits[i] * (hits[i] - 1) / 2 for i in range(4)]

        dfc = self.para_info.value('dfc', '值')
        dfc_ign = xzq_val[self.xzq_info.col_index['dfc_ign']] + self.para_info.value('dfc_ign', '值')
        dfc_ign_crit = self.para['dfc_ign_crit']
        self.para['dfc_rate'] = 375 / (375 + dfc * np.maximum(1 - dfc_ign, 0))
        self.para['dfc_rate_crit'] = 375 / (375 + dfc * np.maximum(1 - dfc_ign - dfc_ign_crit, 0))
        self.para['anger_rate'] = (self.para_info.value('anger', '值') + 1000) / 2000

        max_rtn = 0
        max_mfq = 0

        for x in trange(self.mfq_info.data.shape[1]):
            para = self.para.copy()
            for y in self.mfq_info.row_index:
                i1 = self.xzq_info.col_index[y]
                i2 = self.mfq_info.row_index[y]
                para[y] = xzq_val[i1] + self.mfq_info.data[i2][x]
            para['atk'] += para['atk_bonus'] * atk_base
            # 剑圣连击转暴击
            if combo_to_crit >= 0:
                para['crit'] += para['combo']
                para['combo'] = 0
            # 属性上限处理
            para_upper = {'crit': 1, 'combo': 1, 'crit_dam': 3}
            for key, value in para_upper.items():
                para[key] = np.minimum(para[key], value)
            # 箭矢额外连携
            para['conti_delta'] = conti_delta.copy()
            if para['arrow'] == 1:
                for i in range(3):
                    para['conti_delta'][i] += (hits[i] - 1) * para['combo'] * 0.01

            rtn = calc_core(para)
            # 属性限制
            for key, value in para_limit.items():
                if key in para and value > 0:
                    rtn *= para[key] >= value * 0.9999

            max_rtn = np.maximum(max_rtn, rtn)
            max_mfq = max_mfq * (max_rtn != rtn) + x * (max_rtn == rtn)
        max_inx = np.argsort(-max_rtn)[:result_num]

        results = []
        mfq = self.mfq.mfq_arr.transpose()
        for x in max_inx:
            if max_rtn[x] <= 0:
                continue
            debug_para = {}
            for y in self.mfq_info.row_index:
                i1 = self.xzq_info.col_index[y]
                i2 = self.mfq_info.row_index[y]
                debug_para[self.mfq.mfq_name_map[y]] = round(xzq_val[i1][x] + self.mfq_info.data[i2][max_mfq[x]], 4)
            debug_para['攻击'] = int(debug_para['攻击'] + debug_para['基础攻击'] * atk_base)
            del debug_para['基础攻击']
            result = {"0心之器": xzq_arr[x]}
            if self.mfq_choice >= 0:
                result['1魔法器主词条'] = self.mfq.mfq_print(mfq[max_mfq[x]])['主词条']
                result['2魔法器随机词条'] = self.mfq.mfq_print(mfq[max_mfq[x]])['随机词条']
            result['3属性'] = debug_para
            result['4总伤害'] = int(max_rtn[x])
            results.append(result)
        return results


if __name__ == '__main__':
    import time

    print('【当前环境】algo测试v3.0.1')
    t = time.time()
    sol = Solver()
    sol.load_xzq("心之器.xlsx")
    sol.load_role("角色.xlsx")
    sol.load_mfq("角色.xlsx", 0, 0.8, 9)
    ans = sol.calc_xzq(5, set())
    print(time.time() - t)
    for xx in ans:
        for yy in xx:
            print(yy[1:])
            print(xx[yy])
        print()
