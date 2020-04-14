from planet import Planet
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Population Growth', artist='Marianopolis Programming Club',
                comment='Cool Animation!')
writer = FFMpegWriter(fps=15, metadata=metadata)


planet = Planet()
fig = plt.figure()
plt.title("Growth of population over time")

# initial_population = int(input("Initial population: "))
# population_growth_rate = float(input("Growth rate: "))
file_output_name = input("Video output name: ")
number_of_days = int(input("Number of days that you want to run the simulation: "))

# planet.population = initial_population
# planet.population_growth_rate = population_growth_rate

with writer.saving(fig, (file_output_name + ".mp4"), number_of_days):
    for i in range(number_of_days):
        planet.step()
        planet.render()
        writer.grab_frame()