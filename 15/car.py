class Car():
	"""자동차를 표현"""
	def __init__(self, make, model, year):
		"""자동차를 나타내는 속성 초기화"""

	def get_descriptive_name(self):
		"""읽기 쉽고 의미있는 이름을 반환한다."""
		#e.g. 2017 KIA sorento
	
	def read_odometer(self):
		"""자동차의 주행거리를 출력한다."""
		#e.g. This car has 5000 km on it
	 
	def update_odometer(self, km):
		"""주행거리 표시기를 주어진 값으로 바꾼다.
		주행거리를 더 작은 값으로 되돌리려는 시도는 거부한다."""
	
	def increment_odometer(self, km):
		"""주행거리를 주어진 양만큼 늘린다."""
		

# 전기자동차의 특징을 표현한 Battery 클래스
"""
	다음과 같은 메서드를 만들고 각 메서드별로 doc string 달 것.
	init: 배터리 사이즈의 기본 값은 70, 배터리 속성을 초기화 한다.
	describe_battery : 배터리 크기를 설명하는 문장 출력
	get_range : 이 배터리가 제공하는 주행 가능 거리 출력
				배터리 사이즈가 70이면 240km, 85면 270km
			
"""

# 전기자동차에만 해당하는 ElectricCar 클래스
"""
	Car 클래스를 상속.
	init : make, model, year에 관해서는 부모(super)클래스의 init method 사용
		   battery는 위에서 만든 battery 클래스의 인스턴스로 초기화
"""

# Battery와 ElectricCar 클래스를 electric_car.py 모듈로 따로 정리하자.
