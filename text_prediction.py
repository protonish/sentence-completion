import subprocess

#model = 'cv2000/lm_lstm_epoch998.17_5.5777.t7'
#pretext = 'the common man '

def predict_sent(model, pretext):
	text = subprocess.check_output(['th','predict.lua', model, pretext])
	return text.strip()

print predict_sent(model, pretext)
