import math
class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items

        self.page_size = page_size

        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"page_num must be between 1 and {self.total_pages}")
        self.current_idx = page_num - 1
        return self  

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        # if there are 0 pages, keep index at 0
        self.current_idx = max(self.total_pages - 1, 0)
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
p = Pagination(list(range(1, 26)), page_size=10)

print(p.get_visible_items())      
print(p.next_page().get_visible_items())  
print(p.last_page().get_visible_items()) 

p.go_to_page(2)
print(p.get_visible_items())          
