#####################
# ���� ���� vs ���� ����
#####################
scores = [10, 20, 30, 40, 50]
print("scores ����Ʈ", scores)
print("scores address", id(scores))

#####################
# ����Ʈ ����
#####################
values1 = scores  # ����Ʈ ����
print("values1 ����Ʈ", values1)
print("values1 address", id(values1))

#####################
# ����Ʈ ����
#####################
values2 = list(scores)  # ����Ʈ ����
print("values2 ����Ʈ", values2)
print("values2 address", id(values2))
