import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-l10n-iran",
    description="Meta package for oca-l10n-iran Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-l10n_ir_accounting>=16.0dev,<16.1dev',
        'odoo-addon-l10n_ir_hr_contract>=16.0dev,<16.1dev',
        'odoo-addon-l10n_ir_states>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
