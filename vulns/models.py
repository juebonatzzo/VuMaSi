from django.db import models

VULNERABILITY_STATES = [
    (0, 'Created'),
    (10, 'Study'),
    (20, 'Reported'),
    (30, 'Monitoring'),
    (40, 'Closed'),
]

VULNERABILITY_IMPACT = [
    (0, 'Informational'),
    (10, 'Low'),
    (20, 'Medium'),
    (30, 'High'),
    (40, 'Critical'),
]


class Vulnerability(models.Model):
    name = models.CharField(max_length=200, unique=True)
    state = models.IntegerField(choices=VULNERABILITY_STATES, default=0,)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True)
    impact = models.IntegerField(choices=VULNERABILITY_IMPACT, default=0)
    exploited_in_the_wild = models.BooleanField(default=False)
    solution = models.TextField(null=True)
    notes = models.TextField(null=True)
    # links
    # attack_vector
    # vulnerable_products
    # affectation

    class Meta:
        verbose_name_plural = "Vulnerabilities"

    def __str__(self):
        return self.name


class CVE(models.Model):
    cve_id = models.CharField(max_length=30, unique=True)
    cve_cvss_score = models.FloatField(null=True, blank=True)
    cve_cvss_vector = models.CharField(max_length=100, null=True, blank=True)

    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='cves')

    def __str__(self):
        return self.cve_id
