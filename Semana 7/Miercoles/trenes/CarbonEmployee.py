from Employee import Employee

class CarbonEmployee(Employee):
    def __init__(self, name, dni, hours):
        super().__init__(name, dni, hours)
        self.rate=30
    
    def pago_horas(self):
        if self.hours > 8:
            self.pago=self.rate*(1+0.3)*self.hours
            return self.pago
        else:
            self.pago=self.rate*self.hours
            return self.pago


