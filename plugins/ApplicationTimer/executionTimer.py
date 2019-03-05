import time


class ExecutionTimer:
	def __init__(self):
		self.start = None
		self.end = None

	def start_timer(self):
		self.start = time.time()
		return

	def end_timer(self):
		self.end = time.time()
		return

	def elapsed_time(self):
		total_ms = int(self.end - self.start)
		secondes = (total_ms / 1000) % 60
		secondes = int(secondes)
		minutes = (total_ms / (1000 * 60)) % 60
		minutes = int(minutes)
		hours = (total_ms / (1000 * 60 * 60)) % 24
		hours = int(hours)
		return "{} Heures  {} Minutes  {} Secondes".format(hours, minutes, secondes)
