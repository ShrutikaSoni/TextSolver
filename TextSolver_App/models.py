from djongo import models
from datetime import datetime

# Create your models here.
class Text(models.Model):
  inp_text =models.CharField(max_length=100)
  output_text=models.CharField(max_length=100)
  date=models.DateField(auto_now_add=True)

  def  __str__(self):
     return self.inp_text