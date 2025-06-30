from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    is_open = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class StoreTiming(models.Model):
    DAYS = [
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
        ("SUN", "Sunday"),
    ]
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='timings')
    day = models.CharField(max_length=3, choices=DAYS)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.store.name} - {self.day}"
