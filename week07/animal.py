
class Animal:
    def __init__(self,type,figure,character):
        self.type = type
        self.figure = figure
        self.character = character
        if self.type == "食肉" and (self.figure > "中等" or self.figure == "中等") and self.character == "凶猛":
            self.is_ferocious = "凶猛动物"
        else:
            self.is_ferocious = "非凶猛动物"

class Cat(Animal):
    sound = '喵喵'
    is_pet = '宠物'

    def __init__(self,name,type,figure,character):
        super().__init__(type,figure,character)
        self.name = name

class Zoo:

    def __init__(self,name):
        self.name = name

    def add_animal(self,animal_obj):
        animal_category = animal_obj.__class__.__name__
        try:
            super().__getattribute__(animal_category)
            if not animal_obj in self.__dict__[animal_category]:
                (self.__dict__[animal_category]).append(animal_obj)
            else:
                print('已添加，请勿重复添加')
        except Exception as e:
            obj_list = []
            obj_list.append(animal_obj)
            self.__dict__[animal_category] = obj_list





if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')