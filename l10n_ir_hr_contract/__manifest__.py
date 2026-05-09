# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Iran - Employee Contracts",
    "version": "19.0.1.0.0",
    "author": "Fadoo, Odoo Community Association (OCA)",
    "maintainer": ["saeed-raesi"],
    "website": "https://github.com/OCA/l10n-iran",
    "license": "AGPL-3",
    "category": "Localization/Iran",
    "summary": "Iranian HR contract with local allowance fields.",
    "depends": ["hr", "hr_contract"],
    "data": [
        "views/hr_contract_view.xml",
        "views/res_config_settings_inherit.xml",
    ],
    "installable": True,
}
