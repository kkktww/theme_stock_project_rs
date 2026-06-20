import flet as ft
from service import *

def main(page):

    page.title="테마주 분석"

    output=ft.Text()

    def search(e):

        df=StockService.get_theme(1)

        output.value=str(df)

        page.update()

    def report(e):

        df=StockService.get_report(1)

        output.value=str(df)

        page.update()

    page.add(

        ft.Text(
            "테마주 분석 시스템",
            size=30
        ),

        ft.ElevatedButton(
            "테마 조회",
            on_click=search
        ),

        ft.ElevatedButton(
            "재무 분석",
            on_click=report
        ),

        output
    )

ft.app(target=main)