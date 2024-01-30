class Reports:
    def report(self,report_of_inventory):
        print('inventory Report')
        report_of_inventory.display_inventory()

    def category_report(self,report_category):
        print('category Report')
        report_category.display_cat()