import asyncio
import pandas as pd
from pyppeteer import launch


class CompaniesMapping:

    @staticmethod
    async def take_screenshot(company_name, url):
        browser = await launch(
            headless=True,
            executablePath="C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        page = await browser.newPage()

        await page.goto(url)
        await page.screenshot({'path': f'screenshots/{company_name}.png', 'fullPage': True})
        await browser.close()

    @staticmethod
    async def mapping(companies_file):
        df = pd.read_excel(companies_file, engine='openpyxl')
        for index, row in df.iterrows():
            url = row['URL']
            try:
                if url and str(url).startswith('http'):
                    await CompaniesMapping.take_screenshot(df['Company Name'], url)
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")


asyncio.get_event_loop().run_until_complete((CompaniesMapping().mapping('../Careers files/new career.xlsx')))
