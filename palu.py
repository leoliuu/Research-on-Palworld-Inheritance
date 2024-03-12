import random


def generate_offspring(father_attributes, mother_attributes, hidden_attributes, inheritance_probability):
    if inheritance_probability == 0:
        return []  # 返回空列表表示子代无属性

    offspring_attributes = []

    # 遗传父本的属性
    for attribute in father_attributes:
        if random.random() <= inheritance_probability:
            offspring_attributes.append(attribute)

    # 遗传母本的属性
    for attribute in mother_attributes:
        if random.random() <= inheritance_probability:
            offspring_attributes.append(attribute)

    # 随机遗传隐性属性
    num_hidden_attributes = random.randint(0, 4 - len(offspring_attributes))  # 随机选择要遗传的隐性属性数量
    hidden_attributes_inherited = random.sample(hidden_attributes, num_hidden_attributes)

    offspring_attributes.extend(hidden_attributes_inherited)

    return offspring_attributes


hidden_attributes = list(range(1, 51))  # 隐性属性库为数字1-50

while True:
    father_attributes = input("输入父本的属性（以空格分隔）: ").split()
    mother_attributes = input("输入母本的属性（以空格分隔）: ").split()

    father_attributes = list(map(int, father_attributes[:4]))  # 父本属性最多为4个
    mother_attributes = list(map(int, mother_attributes[:4]))  # 母本属性最多为4个

    inheritance_probability = float(input("输入遗传属性的概率（0-1之间）: "))

    # 生成子代属性
    offspring_attributes = generate_offspring(father_attributes, mother_attributes, hidden_attributes,
                                              inheritance_probability)

    # 输出子代属性
    print("子代的属性: ", offspring_attributes)
    print()  # 打印空行以分隔不同的子代生成

    # 询问是否继续生成子代
    choice = input("是否继续测试（y）: ")
    if choice.lower() != 'y':
        break