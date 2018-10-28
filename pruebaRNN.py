import tensorflow as tf
import copy

#Setup of RNN
class Brain(object):
    def __init__(self,nodesInput):
       
        self.inputs = tf.placeholder(shape=[None,nodesInput],dtype=tf.float32)
        self.W1 = tf.Variable(tf.random_normal(shape=[nodesInput,1]))
        self.tensor = tf.Variable(0.4)
        self.tensor2 = tf.Variable(255.21)
        
        #Sesion en donde se almacenaran y procesaran los datos
        self.sess = tf.Session()

        #Inicializar variables y pesos
        self.init = tf.global_variables_initializer()
        self.sess.run(self.init)

    def predict(self):
        predict = self.sess.run(self.tensor)
        return predict
    
    def setTensor(self,brainCopy):

        tensor = tf.Variable(tf.identity(brainCopy.tensor2))

        assignT = tf.assign(self.tensor,tensor)

        init = tf.global_variables_initializer()
        self.sess.run(init)

        self.sess.run(assignT)
        

brain = Brain(1)
brain2 = Brain(1)


print(brain.predict())

print(brain2.predict())

brain2.setTensor(brain)
print(brain.predict())
print(brain2.predict())

