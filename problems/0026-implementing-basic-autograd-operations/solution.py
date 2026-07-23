class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
    def __repr__(self):
        def fmt(x):
            return int(x) if float(x).is_integer() else round(x, 4)
        return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

    def __add__(self, other):
        x = self.data + other.data
        res = Value(x, (self, other), '+')
        def _backward():
            self.grad += res.grad * 1
            other.grad += res.grad * 1
        res._backward = _backward
        return res
        

	def __mul__(self, other):
		x = self.data * other.data
		res = Value(x, (self, other), '*')
		def _backward():
			self.grad += res.grad * other.data
			other.grad += res.grad * self.data
		res._backward = _backward
		return res

	def relu(self):
		if self.data > 0:
			x = self.data
		else:
			x = 0
		res = Value(x, (self,), 'ReLU')
		def _backward():
			if self.data > 0:
				self.grad += res.grad
			else:
				self.grad += 0
		res._backward = _backward
		return res


	def backward(self):
		topo = []
		visited = set()
		def build_topo(v):
			if v not in visited:
				visited.add(v)
				for child in v._prev:
					build_topo(child)
				topo.append(v)
		build_topo(self)
		self.grad = 1
		for v in reversed(topo):
			v._backward()