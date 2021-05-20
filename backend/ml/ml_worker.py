from multiprocessing import Pipe, Process


class TaskManager():
	pipe = None
	process = None

	@classmethod
	def setup(cls):
		if cls.pipe is None and cls.process is None:
			parent, child = Pipe()

			process = Process(target=run, args=(child,))
			process.daemon = True
			process.start()
			cls.pipe = parent
			cls.process = process

	@classmethod
	def predict_gender(cls, *args, **kwargs):
		cls.pipe.send({'args': args, "kwargs": kwargs, "task_name": "predict_gender"})
		result = cls.pipe.recv()
		return result

	@classmethod
	def extract_vector(cls, *args, **kwargs):
		cls.pipe.send({"args": args, "kwargs": kwargs, "task_name": "extract_vector"})
		result = cls.pipe.recv()
		return result

	@classmethod
	def face2vector(cls, *args, **kwargs):
		"""
		:param images: in BGR color space
		:param return_list: If True return type "list" else return type "np.ndarray"
		:return: 128 dimensional vector
		"""
		cls.pipe.send({"args": args, "kwargs": kwargs, "task_name": "face2vector"})
		result = cls.pipe.recv()
		return result

	@classmethod
	def close_process(cls):
		cls.process.terminate()


def run(pipe):
	from ml.gender import GenderModel
	from ml.recognition import FaceRecognition

	class MlWorker:
		def __init__(self, pipe):
			self.pipe = pipe
			self.facenet = FaceRecognition()
			self.gendernet = GenderModel()

		def run(self):
			while True:
				task = self.pipe.recv()
				args, kwargs, task_name = task['args'], task['kwargs'], task['task_name']
				if hasattr(self.facenet, task_name):
					func = self.facenet.__getattribute__(task_name)
					result = func(*args, **kwargs)
					self.pipe.send(result)
				elif hasattr(self.gendernet, task_name):
					func = self.gendernet.__getattribute__(task_name)
					self.pipe.send(func(*args, **kwargs))

	ml_worker = MlWorker(pipe=pipe)
	ml_worker.run()
