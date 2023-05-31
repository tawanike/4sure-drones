from django.test import TestCase, Client
from drones.models import Drone, DroneStatusMovement, BatteryStatus
from decimal import Decimal

from medication.models import Medicine
# Create your tests here.


class DroneModelTestCase(TestCase):
    def setUp(self) -> None:
        self.drone_one = {
            "serial_number": "ZKIM110522",
            "model": "heavyweight",
            "state": "idle",
            "weight_limit": Decimal(500),
            "battery_capacity": 100
        }
        self.drone_two = {
            "serial_number": "VM190591",
            "model": "lightweight",
            "state": "idle",
            "weight_limit": Decimal(150),
            "battery_capacity": 20
        }

        Drone.objects.create(**self.drone_one)
        Drone.objects.create(**self.drone_two)

    def test_can_create_drone(self):
        drones = Drone.objects.all()
        self.assertEqual(drones.count(), 2)

    def test_initial_drone_status_movement_added(self):
        drone_one = DroneStatusMovement.objects.filter(
            drone__serial_number=self.drone_one['serial_number'])

        self.assertEquals(drone_one.count(), 1)

    def test_initial_drone_battery_level_added(self):
        drone_two = BatteryStatus.objects.filter(
            drone__serial_number=self.drone_one['serial_number'])

        self.assertEquals(drone_two.count(), 1)


class DroneAPIEndpointTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.drone_one = {
            "serial_number": "ZKIM110522",
            "model": "heavyweight",
            "state": "idle",
            "weight_limit": Decimal(500),
            "battery_capacity": 100
        }
        self.drone_two = {
            "serial_number": "VM190591",
            "model": "lightweight",
            "state": "idle",
            "weight_limit": Decimal(150),
            "battery_capacity": 20
        }

        self.drone_three = {
            "serial_number": "TAM200388",
            "model": "lightweight",
            "state": "loaded",
            "weight_limit": Decimal(150),
            "battery_capacity": 80
        }

        self.medication = {
            "name": "Telfast",
            "weight": 150,
            "code": "CRA03186",
            "image": "static/medication/download.jpeg"
        }

    def test_list_all_drones_success(self):
        response = self.client.get('/v1/drones')
        self.assertEqual(response.status_code, 200)

    def test_register_drone_success(self):
        response = self.client.post('/v1/drones', self.drone_one)
        self.assertEqual(response.status_code, 201)

    def test_register_drone_with_duplicate_serial_number(self):
        self.client.post('/v1/drones', self.drone_one)
        response_two = self.client.post('/v1/drones', self.drone_one)
        self.assertEqual(response_two.status_code, 400)

    def test_drone_can_be_loaded(self):
        drone = Drone.objects.create(**self.drone_one)
        medication = Medicine.objects.create(**self.medication)
        print(drone)
        print(medication)
        load = {
            "drone": drone.id,
            "payload": medication.id
        }

        response = self.client.post(f'/v1/drones/{drone.id}/load', load)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_drone_can_not_in_idle_state(self):
        drone = Drone.objects.create(**self.drone_three)
        medication = Medicine.objects.create(**self.medication)
        print(drone)
        print(medication)
        load = {
            "drone": drone.id,
            "payload": medication.id
        }

        response = self.client.post(f'/v1/drones/{drone.id}/load', load)
        print(response.json())
        self.assertEqual(response.status_code, 400)
