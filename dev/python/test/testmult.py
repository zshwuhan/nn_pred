## initial test script for applying a multi-layer neural network on time series data
execfile('/omp/startup.py')

g = generator('default', 'default', 'default')
#g.generate_signal('noplot', 'mult_test1.txt')
#g.generate_signal('noplot', 'mult_test2.txt', amplitude_number_changes = 1, amplitude_alpha = 1, phase_number_changes = 1)
#g.generate_signal('noplot', 'mult_test3.txt', amplitude_number_changes = 10, amplitude_alpha = 1, phase_number_changes = 10)

# ----- define streamer -----
#stre = [streamer('/omd/mem_track_2012-08-15T01:53:43.911923.txt'), streamer('/omd/cpu_track_2012-08-15T01:53:43.911923.txt')]
#stre = [streamer('/omd/mult_test1.txt'), streamer('/omd/mult_test2.txt')]
#stre = [streamer('/omd/mult_test1.txt'), streamer('/omd/mult_test2.txt'), streamer('/omd/mult_test3.txt')]
stre = [streamer('/omd/mult_test2.txt')]

# ----- 
lr = 0.1   # learning rate
indim = len(stre)
contextlen = 500
insz = contextlen*indim  # input window size of the NN
nh1 = 50                 # number of hidden units on layer 1
nh2 = indim              # number of hidden units on layer 2
nh3 = indim              # number of hidden units on layer 3
predhorizon = 50
plotint = 5
weightcost = 0.01
alpha = 1e2#1.5e1
beta = 1e3#1.5e4
quiet_steps = 1e3

# ----- define neural network -----
l1 = layer(insz, nh1, nntanh(), 0.01*randn(insz*nh1+nh1))
l2 = layer(nh1, nh2, nntanh(), 0.01*randn(nh1*nh2+nh2))
l3 = layer(nh2, nh3, nntanh(), 0.01*randn(nh2*nh3+nh3))

nn = net([l1, l2], 'mse'); nn.gradcheck(1e-7, 50)

# ----- define trainer -----
#trainer = nnstreamtrainer(nn, stre, lr, contextlen, predhorizon, plotint, weightcost, alpha, beta, quiet_steps)

# ----- start simulation -----
#trainer.nnlearnstream('plot')
