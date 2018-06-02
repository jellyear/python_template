import turtle

class Geobuk(turtle.Turtle):
	def __init__(self):
		# 거북이 모양으로 바꾸고 크기를 가로, 세로 두배로 확장해보자.
		# 확장할 때는 shapesize(가로 몇배, 세로 몇배) 메소드를 쓰면 된다.
		self.radians() # 각도 지정을 호도법으로 변경
		# 청소기로 청소 하는 느낌 내기 위해 색 변경
		self.width(10)
		self.getscreen().bgcolor('gray')
		self.pencolor('white')
		
	def hit_wall(self):
		"""지금 위치한 지점에서 전진해서 벽에 닿는 지점(경계선)까지 거북이를 이동시키고 벽에 닿았을 때 방향을 중심 방향으로 변경한다."""
	
	def run(self):
		while True:
			self.hit_wall()
		
