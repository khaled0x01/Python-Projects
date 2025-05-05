class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate_value = fuelRate  
        self.velocity_value = velocity  
        self.fuelRate = fuelRate
        self.velocity = velocity
    
    @property
    def fuelRate(self):
        return self.fuelRate_value
    
    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self.fuelRate_value = value
        else:
            print("Fuel rate must be between 0 and 100")
    
    @property
    def velocity(self):
        return self.velocity_value
    
    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self.velocity_value = value
        else:
            print("Velocity must be between 0 and 200")
    
    def run(self, velocity, distance):
        self.velocity = velocity
        self.driving_velocity = velocity  # Store for lateness check
        print(f"Car is running at {self.velocity} km/h towards destination")
        
        fuel_consumed = distance  #Fuel Rate decrease by 10% every 10km distance.
        remaining_fuel = self.fuelRate - fuel_consumed
        
        if remaining_fuel <= 0:
            # Calculate distance traveled with available fuel
            distance_traveled = self.fuelRate
            self.fuelRate = 0
            self.stop(distance - distance_traveled)
        else:
            self.fuelRate = remaining_fuel
            self.stop(0)
    
    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped! Out of fuel. {remaining_distance} km remaining to destination.")
        else:
            print("Car stopped! Arrived at destination.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self):
        self.car.run(self.car.velocity, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)

    def send_mail(self):
        print(f"Email sent from {self.email}")



class Office:
    employees_num = 0
    
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None
    
    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1
    
    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employees_num -= 1
            return True
        return False
    
    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction
            return True
        return False
    
    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward
            return True
        return False
    
    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if not emp:
            return False
        
        target_hour = 9  # Need to arrive by 9:00
        is_late = Office.calculate_lateness(target_hour, move_hour, emp.distanceToWork, emp.car.driving_velocity)
        
        if is_late:
            self.deduct(emp_id, 10)
            print(f"{emp.name} is late! 10 LE deducted from salary.")
        else:
            self.reward(emp_id, 10)
            print(f"{emp.name} is on time! 10 LE added to salary.")
        return is_late
    
    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        if velocity == 0:
            return True  # Can't move, definitely late
        
        time_needed = distance / velocity  # in hours
        arrival_hour = move_hour + time_needed
        
        return arrival_hour > target_hour


# Test the implementation

fiat_128 = Car(name="Fiat 128", fuelRate=100, velocity=60)
khaled = Employee(name="Khaled", money=1000, mood="neutral", healthRate=100, emp_id=1, car=fiat_128, email="khaled@iti.com", salary=5000, distanceToWork=20)
iti_office = Office(name="ITI Smart Village")
iti_office.hire(khaled)

khaled.sleep(7)
print(f"After sleeping: {khaled.mood}")
khaled.eat(2)
print(f"After eating: {khaled.healthRate}%")
khaled.buy(2)
print(f"After buying: {khaled.money} LE")
khaled.work(8)
print(f"After working: {khaled.mood}")
khaled.refuel(30)
print(f"After refueling: {khaled.car.fuelRate}")
khaled.drive()
print(f"Fuel rate after driving: {khaled.car.fuelRate}")
iti_office.check_lateness(emp_id=1, move_hour=8)
print(f"After lateness check: {khaled.salary}")