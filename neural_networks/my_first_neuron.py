# This is my first neuron based on the Neural Networks from Scratch book
# Chapter 2 - page 27

inputs = [1,2,3,4]
weights = [[0.2,0.8,0.6,-0.5],]
bias = [2,]

#output = (inputs[0]*weights[0] +
#          inputs[1]*weights[1] +
#          inputs[2]*weights[2] +
#          inputs[3]*weights[3] + bias)

#print ( "The result of the initial calculation is: %r" %output)

# ========================================================== #
#                       LOOP UTILIZATION                     #
# ========================================================== #
# As I didn't come up with my own solution this one is taken from
# the book - Chapter 2, page 33
# ========================================================== #
# Note: the loop here is used for calculating the neurons that
# are a part of a layer.

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, bias):
    # Zeroed output for a given neuron
    neuron_output = 0
    
    # Iterate over each input and weight of the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply the input by the associated weght
        # and add to the neuron's output total
        neuron_output += n_input*weight

    # Add the bias to the total
    neuron_output += neuron_bias
    #Put neuron's result in the layer's list
    layer_outputs.append(neuron_output)


print ("Here are the results after the loop: %r" %layer_outputs)
