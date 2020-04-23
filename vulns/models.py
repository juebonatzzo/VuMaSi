from django.db import models

VULNERABILITY_STATES = [
    (0, 'Created'),
    (10, 'Study'),
    (20, 'Reported'),
    (30, 'Monitoring'),
    (40, 'Closed'),
]


class Vulnerability(models.Model):
    name = models.CharField(max_length=200, unique=True)
    state = models.IntegerField(choices=VULNERABILITY_STATES, default=0,)


class CVE(models.Model):
    cve_id = models.CharField(max_length=30, unique=True)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='cves')


