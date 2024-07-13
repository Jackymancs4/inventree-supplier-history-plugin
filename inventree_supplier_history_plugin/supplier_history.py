"""Sample implementation for ActionMixin."""

from plugin import InvenTreePlugin
from plugin.mixins import EventMixin, ActionMixin, APICallMixin, SettingsMixin


class SupplierHistoryPlugin(EventMixin, InvenTreePlugin):
    """An EXTREMELY simple action plugin which demonstrates the capability of the ActionMixin class."""

    NAME = 'SupplierHistoryPlugin'
    SLUG = 'supplier_history'
    TITLE = 'SupplierHistory'

    def wants_process_event(self, event):
        """Return whether given event should be processed or not."""
        return event == 'part_supplierpricebreak.saved' or event == 'part_supplierpart.saved'

    def process_event(self, event, *args, **kwargs):
        print(f"Processing triggered event: '{event}'")
        print('args:', str(args))
        print('kwargs:', str(kwargs))