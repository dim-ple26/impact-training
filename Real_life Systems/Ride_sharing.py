import math;
class RideSharingSystem:
  

  def __init__(self):
     self.drivers=[];
     self.riders=[];
     self.ongoing_rides={}
     
     
  
  def registerDriver(self,driver_ID:int,d_location: [int,int]):
    self.drivers.append((driver_ID,d_location))
    print(f"Driver {driver_ID} is registered at Location {d_location} ")



  def registerRider(self,riderID:int,r_location:[int,int]):
    self.riders.append((riderID,r_location))
    print(f"Rider {riderID} is finding driver at Location {r_location}") 
    
    
    
  def requestRide(self,riderID:int,destination:[int,int]):
      if not self.drivers:
        print("Currently, No driver is Available....We will Update You about Availability")
        return -1;
        
        
        
      rider_location = None
      for r_id, r_location in self.riders:
            if r_id == riderID:
                rider_location = r_location
                break

      if rider_location is None:
        print(f"Rider {riderID} is not registered.")
        return -1

        
        
      min_distance = float('inf');
      closest_driver=None
    
    
      for driver_ID,d_location in self.drivers:
        distance = math.sqrt((d_location[0] - r_location[0])**2 + (d_location[1] - r_location[1])**2)
      
        if distance < min_distance:
          min_distance=distance;
          closest_driver= (driver_ID,d_location);
        
      if closest_driver:
        driver_ID,driver_location = closest_driver
        print(f"Closest driver to rider {riderID} is {driver_ID} ")
        print(f"Driver will drop at location {destination}")
        self.drivers.remove(closest_driver)  
        self.ongoing_rides[riderID] = (driver_ID,destination)
      # this ride is working driver is not free
      
        return f"Driver {driver_ID} is droping"



  
  def endRide(self,driver_ID:int):
     riderID = None
     destination = None
     # finds rider who is on the way with the driver
     for r_id, ride_info in self.ongoing_rides.items():
        if ride_info[0] == driver_ID:
            riderID = r_id
            destination = ride_info[1]
            break

     if riderID is None:
        return f"No active ride found for driver {driverID}."
        
     self.drivers.append((driver_ID,destination))
    
     del self.ongoing_rides[riderID]
     
     return f"ride has ended"



system=RideSharingSystem()
system.registerDriver(1,[0,0])
system.registerDriver(2,[5,5])
system.registerRider(101,[1,1])
print(system.requestRide(101,[10,10]))
print(system.endRide(1))



