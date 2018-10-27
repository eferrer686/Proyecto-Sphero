import tensorflow as tf
import copy

#Setup of RNN
class Brain(object):
    def __init__(self,nodesInput,nodesHidden,nodesOutput):
       
        self.inputs = tf.placeholder(shape=[None,nodesInput],dtype=tf.float32)

        self.W1 = tf.Variable(tf.random_normal(shape=[nodesInput,nodesHidden]))
        self.b1 = tf.Variable(tf.random_normal(shape=[nodesHidden]))
        self.hidden_1 = tf.nn.sigmoid(tf.add(tf.matmul(self.inputs,self.W1),self.b1))

        self.W2 = tf.Variable(tf.random_normal(shape=[nodesHidden,nodesOutput]))
        self.b2 = tf.Variable(tf.random_normal(shape=[nodesOutput]))
        self.output = tf.nn.sigmoid(tf.add(tf.matmul(self.hidden_1,self.W2),self.b2))

        #Mutaciones de red Neural
        #Mutar W1
        self.rW = tf.Variable(tf.random_uniform(self.W1.shape,0,0.5),validate_shape=False)
        self.newW = tf.multiply(self.W1,self.rW)
        self.mutateW1 = tf.assign(self.W1,self.newW)

        #Mutar W2
        self.rW = tf.Variable(tf.random_uniform(self.W2.shape,0,0.5),validate_shape=False)
        self.newW = tf.multiply(self.W2,self.rW)
        self.mutateW2 = tf.assign(self.W2,self.newW)

        #Mutar b1
        self.rW = tf.Variable(tf.random_uniform(self.b1.shape,0,0.5),validate_shape=False)
        self.newW = tf.multiply(self.b1,self.rW)
        self.mutateb1 = tf.assign(self.b1,self.newW)

        #Mutar b2
        self.rW = tf.Variable(tf.random_uniform(self.b2.shape,0,0.5),validate_shape=False)
        self.newW = tf.multiply(self.b2,self.rW)
        self.mutateb2 = tf.assign(self.b2,self.newW)


        #Sesion en donde se almacenaran y procesaran los datos
        self.sess = tf.Session()

        #Inicializar variables y pesos
        self.init = tf.global_variables_initializer()
        self.sess.run(self.init)

    def predict(self,input):
        predict = self.sess.run(self.output,feed_dict={self.inputs:input})
        return predict

    def mutate(self,randomRate = 0.5):
        #Mutar Red Neural
        self.sess.run(self.mutateW1)
        self.sess.run(self.mutateW2)
        self.sess.run(self.mutateb1)
        self.sess.run(self.mutateb2)

    def clone(self):

        inputs = self.inputs

        W1 = tf.identity(self.W1)
        b1 = tf.identity(self.b1)
        hidden_1 = tf.identity(self.hidden_1)
        
        W2 = tf.identity(self.W2)
        b2 = tf.identity(self.b2)
        output = tf.identity(self.output)
        
        return inputs,W1,b1,hidden_1,W2,b2,output
    
    def copy(self,inputs,W1,b1,hidden_1,W2,b2,output):
        #Copy from another brain
        self.sess.run(tf.global_variables_initializer())

        self.copyinputs = tf.assign(self.inputs,inputs)

        self.copyW1 = tf.assign(self.W1,W1)
        self.copyb1 = tf.assign(self.b1,b1)
        self.copyh1 = tf.assign(self.hidden_1,hidden_1)

        self.copyW2 = tf.assign(self.W2,W2)
        self.copyb2 = tf.assign(self.b2,b2)
        self.copyoutput = tf.assign(self.output,output)

        self.sess.run(tf.global_variables_initializer())

        self.sess.run(self.copyinputs)

        self.sess.run(self.copyW1)
        self.sess.run(self.copyb1)
        self.sess.run(self.copyh1)

        self.sess.run(self.copyW2)
        self.sess.run(self.copyb2)
        self.sess.run(self.copyoutput)
        
    
    def setAll(self,inputs,W1,b1,hidden_1,W2,b2,output):
        self.inputs = inputs

        self.W1 = W1
        self.b1 = b1
        self.hidden_1 = hidden_1

        self.W2 = W2
        self.b2 = b2
        self.output = output
        
    
    def printVariables(self):
        print(self.sess.run(self.W1))
        print(self.sess.run(self.b1))
        print(self.sess.run(self.W2))
        print(self.sess.run(self.b2))

brain = Brain(4,5,1)

brain.predict([[1,1,1,1]])