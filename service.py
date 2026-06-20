from repository import *

stock=StockRepository()
join=JoinRepository()

class StockService:

    def get_theme(theme):

        return stock.find_by_theme(
            theme
        )

    def get_report(theme):

        return join.theme_report(
            theme
        )