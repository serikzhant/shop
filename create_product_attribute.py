from oscar.apps.catalogue.models import *


material = AttributeOptionGroup.objects.create(
    name="Material"
)
color = AttributeOptionGroup.objects.create(
    name="Color"
)


AttributeOption.objects.create(
    group= material,
    option= "Plastic",
)

AttributeOption.objects.create(
    group= material,
    option= "Rubber",
)
AttributeOption.objects.create(
    group= material,
    option= "Wood"
)


AttributeOption.objects.create(
    group= color,
    option= "Red",
)

AttributeOption.objects.create(
    group= color,
    option= "Blue",
)

AttributeOption.objects.create(
    group= color,
    option= "Black"
)

print("success")