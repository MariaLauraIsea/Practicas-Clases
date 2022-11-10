from Employee import Employee

class BulletEmployee(Employee):
    def __init__(self, name, dni, hours):
        super().__init__(name,dni,hours)
        self.rate=60


    def pago_horas(self):
        if self.hours > 8:
            pago=self.rate*(1+0.3)*self.hours
            return pago
        return self.rate*self.hours