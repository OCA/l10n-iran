# Part of Odoo. See LICENSE file for full copyright and licensing details.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Iran - Accounting",
    "version": "17.0.1.0.0",
    "countries": ["ir"],
    "category": "Accounting/Localizations/Account Charts",
    "summary": """iran accounting chart and localization.""",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/l10n-iran",
    "depends": ["account"],
    "data": [
        "data/res_currency_data.xml",
        "data/res.bank.csv",
    ],
}
