import tensorflow as tf


#Setup of RNN
class Brain(object):
    def __init__(self,nodesInput,nodesHidden,nodesOutput):

        self.randomRate = 0.5
       
        self.inputs = tf.placeholder(shape=[None,nodesInput],dtype=tf.float32)

        self.W1 = tf.Variable(tf.random_normal(shape=[nodesInput,nodesHidden]))
        self.b1 = tf.Variable(tf.random_normal(shape=[nodesHidden]))
        self.hidden_1 = tf.nn.sigmoid(tf.add(tf.matmul(self.inputs,self.W1),self.b1))

        self.W2 = tf.Variable(tf.random_normal(shape=[nodesHidden,nodesOutput]))
        self.b2 = tf.Variable(tf.random_normal(shape=[nodesOutput]))
        self.output = tf.nn.sigmoid(tf.add(tf.matmul(self.hidden_1,self.W2),self.b2))

        #Mutaciones de red Neural
        #Mutar W1
        self.rW = tf.Variable(tf.random_uniform(self.W1.shape,0,self.randomRate),validate_shape=False)
        self.newW = tf.multiply(self.W1,self.rW)
        self.mutateW1 = tf.assign(self.W1,self.newW)

        #Mutar W2
        self.rW = tf.Variable(tf.random_uniform(self.W2.shape,0,self.randomRate),validate_shape=False)
        self.newW = tf.multiply(self.W2,self.rW)
        self.mutateW2 = tf.assign(self.W2,self.newW)

        #Mutar b1
        self.rW = tf.Variable(tf.random_uniform(self.b1.shape,0,self.randomRate),validate_shape=False)
        self.newW = tf.multiply(self.b1,self.rW)
        self.mutateb1 = tf.assign(self.b1,self.newW)

        #Mutar b2
        self.rW = tf.Variable(tf.random_uniform(self.b2.shape,0,self.randomRate),validate_shape=False)
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
        self.randomRate = randomRate
        #Mutar Red Neural
        self.sess.run(self.mutateW1)
        self.sess.run(self.mutateW2)
        self.sess.run(self.mutateb1)
        self.sess.run(self.mutateb2)


    
    def copy(self,brainClone):
        #Copy from another brain


        tW1 = tf.Variable(tf.identity(brainClone.sess.run(brainClone.W1)))
        tb1 = tf.Variable(tf.identity(brainClone.sess.run(brainClone.b1)))
        
        tW2 = tf.Variable(tf.identity(brainClone.sess.run(brainClone.W2)))
        tb2 = tf.Variable(tf.identity(brainClone.sess.run(brainClone.b2)))
        
    
        copyW1 = tf.assign(self.W1,tW1)
        copyb1 = tf.assign(self.b1,tb1)
       
        copyW2 = tf.assign(self.W2,tW2)
        copyb2 = tf.assign(self.b2,tb2)
       
        init = tf.global_variables_initializer()
        self.sess.run(init)

        self.sess.run(copyW1)
        self.sess.run(copyb1)
        
        self.sess.run(copyW2)
        self.sess.run(copyb2)
        
    
    def printVariables(self):
        print(self.sess.run(self.W1))
        print(self.sess.run(self.b1))
        print(self.sess.run(self.W2))
        print(self.sess.run(self.b2))

    def destroy(self):
        
        del self