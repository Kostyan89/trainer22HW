# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def __init(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.fly = False
        self.crawl = False
        self.speed = 1

    def unit_move(self, direction):
        if self.fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if self.fly:
            self.speed *= 1.2
            if direction == 'UP':
                new_y = self.y + self.speed
                new_x = self.x
            elif direction == 'DOWN':
                new_y = self.y - self.speed
                new_x = self.x
            elif direction == 'LEFT':
                new_y = self.y
                new_x = self.x - self.speed
            elif direction == 'RIGHT':
                new_y = self.y
                new_x = self.x + self.speed
        if self.crawl:
            self.speed *= 0.5
            if direction == 'UP':
                new_y = self.y + self.speed
                new_x = self.x
            elif direction == 'DOWN':
                new_y = self.y - self.speed
                new_x = self.speed
            elif direction == 'LEFT':
                new_y = self.y
                new_x = self.speed - self.speed
            elif direction == 'RIGHT':
                new_y = self.y
                new_x = self.speed + self.speed

            self.field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
