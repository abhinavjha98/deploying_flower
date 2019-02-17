from commons import get_tensor,get_model

model = get_model()

def get_flower_name(image_bytes):
	tensor = get_tensor(image_bytes)
	outputs = model.forward(tensor)
	_, prediction = outputs.max(1)
	category = prediction.item()
	print(category)