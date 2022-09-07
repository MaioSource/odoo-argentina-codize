{
    "name": "Grupos de Pago con Múltiples Métodos",
    "version": "15.0.1.0.0",
    "category": "Accounting",
    "author": "ADHOC SA, Exemax, Codize, Birtum",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "account_financial_amount",
        "account_payment_fix",
    ],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/account_payment_group_invoice_wizard_view.xml',
        'wizards/res_config_settings_views.xml',
        'views/account_payment_view.xml',
        'views/account_move_line_view.xml',
        'views/account_payment_group_view.xml',
        'views/account_payment_receiptbook_view.xml',
        'views/account_journal_dashboard_view.xml',
        'report/report_payment_group.xml',
        'data/mail_template_data.xml',
    ],
    "demo": [],
}
