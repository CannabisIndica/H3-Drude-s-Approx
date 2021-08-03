import cmath
import random

#The constants involved in a drude's approxiamation equation. The frequency can be in any units.
epsilon_inf = float(input("High energy dielectric constant")) 
omega_p = float(input("Plasma Frequency"))
tau = float(input("Scattering time"))
minfreq = float(input("Minimum Frequency"))
maxfreq = float(input("Maximum Frequency"))
freq_pts = int(input("Frequency points to be defined"))

#Randomly generates the different input angular frequencies
x = freq_pts
omega = []
for i in range(x):
    omega.append(random.uniform(minfreq,maxfreq))

#Generating the matrix and computing real and imaginary parts
def compute(l):
    output = []
    for i in l:
        num = omega_p**2
        den = complex(i**2,i*(tau**(-1)))
        ans = epsilon_inf*(1-(num/den))
        ini = str(i) + ","
        re = str(ans.real) + ","
        im = str(ans.imag) + "\n"
        output.append(ini+re+im)
    return output

x = compute(omega)

with open ("Result.txt","w") as f:
    f.writelines(x)

#credits - Keith Chia Wen Kai 