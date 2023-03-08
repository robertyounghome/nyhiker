from django.db import models

class Range(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Mountain(models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    rating = models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=2)
    range = models.ForeignKey(Range, on_delete=models.CASCADE)

    class Meta:
        ordering = ["range", "name"]

    def __str__(self):
        return f"{self.range} : {self.name}"

    # def planned_for_challenge(self, challenge):
    #     # challenge = Challenge.objects.get(id=id)
    #     return self in challenge.mountains

class Condition(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hike(models.Model):
    name = models.CharField(max_length=50)
    name_small = models.CharField(max_length=10, null=True)
    description = models.TextField(null=True)
    range = models.ForeignKey(Range, on_delete=models.CASCADE, null=True)
    duration = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    rating = models.DecimalField(null=True, decimal_places=1, max_digits=2)
    conditions = models.ManyToManyField(Condition, blank=True)
    mileage = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    gain = models.IntegerField(null=True)
    completed_on = models.DateField("date completed", null=True, blank=True)
    mountains = models.ManyToManyField(Mountain, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    alltrails = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
class TrailLink(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.hike} : {self.name}"
    
class HikePart(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()

    def __str__(self): 
        return f"{self.name}"

class HikeDetail(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    hike_part = models.ForeignKey(HikePart, null=True, on_delete=models.CASCADE) 
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.hike.name} : Part {self.hike_part} : Paragraph {self.order}"

class Challenge(models.Model):
    name = models.CharField(max_length=50)
    name_small = models.CharField(max_length=5)
    description = models.TextField(null=True)
    mountains = models.ManyToManyField(Mountain, blank=True)
    hikes = models.ManyToManyField(Hike, blank=True)
    completed_on = models.DateField("date completed", null=True, blank=True)

    def __str__(self):
        return self.name

