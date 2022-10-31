class TrackOrders:
    def __init__(self):
        self._orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        return self._orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered_dish = None
        most_ordered_dish_count = 0
        for _, order, _ in self._orders:
            if order == most_ordered_dish:
                most_ordered_dish_count += 1
            elif most_ordered_dish_count == 0:
                most_ordered_dish = order
                most_ordered_dish_count = 1
            else:
                most_ordered_dish_count -= 1
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        dishes = set()
        dishes_set = set()
        for cust, order, _ in self._orders:
            if cust == customer:
                dishes.add(order)
            dishes_set.add(order)
        return dishes_set - dishes

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        days_set = set()
        for cust, _, day in self._orders:
            if cust == customer:
                days.add(day)
            days_set.add(day)
        return days_set - days

    def get_busiest_day(self):
        days = {}
        for _, _, day in self._orders:
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for _, _, day in self._orders:
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return min(days, key=days.get)
