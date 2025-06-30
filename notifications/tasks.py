from celery import shared_task
from notifications.services.alert_service import check_and_notify_back_in_stock

@shared_task
def run_stock_alert_notifications():
    check_and_notify_back_in_stock()
