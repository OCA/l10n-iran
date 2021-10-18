# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Iran - Base",
    "version": "14.0.3.0.0",
    "author": "Fadoo, Odoo Community Association (OCA)",
    "maintainer": ["saeed-raesi"],
    "website": "https://github.com/OCA/l10n-iran",
    "license": "AGPL-3",
    "category": "l10n/Technical",
    "summary": "Iran Base Calendar",
    "depends": ["base", "account"],
    "data": ["views/user_preferences.xml", "views/partner_preferences.xml"],
    "external_dependencies": {
        "python": ["jdatetime"],
    },
    "installable": True,
}
