import matplotlib.pyplot as plt
days=['sunday', 'monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
hours_of_sleep=[7,5,7,6,8,4,10]
plt.bar(days, hours_of_sleep)
plt.legend(title='sleep management')
plt.show()