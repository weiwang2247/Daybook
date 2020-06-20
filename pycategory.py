class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """A list of the categories."""
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']],\
                            'income', ['salary', 'bonus']]

    def is_category_valid(self, category, is_category = None):
        """Check if input record_category in the category_list."""
        if is_category == None:
            is_category = self._categories
        if isinstance(is_category, list):
            for i in is_category:
                p = self.is_category_valid(category, i)
                if p == True:
                    return True
        return category == is_category
    
    def find_subcategories(self, category):
        def find_subcategories_gen(category, categories = None, found = False):
            if categories == None:
                categories = self._categories
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category, categories[index + 1], found = True)
            else:
                if categories == category or found == True:
                    yield categories
        return [i for i in find_subcategories_gen(category, categories = None, found = False)]


        
    def view(self):
        """View all the category and its subcategories"""
        def category_gen(view_category = None, level = -1):
            if view_category == None:
                view_category = self._categories
            if (isinstance(view_category, list)) == True:
                for i in view_category:
                    yield from category_gen(i, level+1)
            else:
                yield (f'{" " * 2 * level}- {view_category}')
        return [i for i in category_gen(view_category = None, level = -1)]
                       
               
                       