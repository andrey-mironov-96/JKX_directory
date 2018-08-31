class calculation_data_all_sevices(object):

    def __init__(self):
        self.list_home_services = list()



    def calculation(self):
        import index as home_sevices
        self.list_home_services = home_sevices.collection_of_user_data_about_home_services().return_results_entered_user_data()

        for i in range(3):
            print(self.list_home_services[4]*self.list_home_services[i])



a = calculation_data_all_sevices()
a.calculation()