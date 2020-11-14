available_doctors=['Anesthesiologist','Cardiologist','Dentist','Dermatologist','Orthopedist']
requested_doctors=input('Hello! What type of doctor do you want? ')
if requested_doctors in available_doctors:
	print('We have this type of doctor in the hospital')
else:
	print('Sorry. There is no such type of doctor')
