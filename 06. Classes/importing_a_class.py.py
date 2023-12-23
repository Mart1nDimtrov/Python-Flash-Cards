#We import classes by storing them in a file
#and then listing each class we need.
from trails import Trail, BikeTrail

#An istance of the class represents a specific trail.
verst = Trail("Mt. Verstovia")
print(f"Destination: {verst.dest}.")
verst.describe_trail()
verst.run_trail()