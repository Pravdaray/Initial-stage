import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  #loss=[]
  #dw = []
  num_classes = W.shape[1]
  num_train = X.shape[0]

  for i in xrange(num_train):
   #here we define loss
      scores = np.dot(X[i], W)
      scores -= np.max(scores)
      #softmax = np.exp(scores)/np.sum(np.exp(scores)
      scores_sum = np.sum(np.exp(scores))
      exp_score = np.exp(scores[y[i]])
      # the loss update
      loss += -np.log(exp_score / scores_sum)
      # the gradient update
      dW[:, y[i]] -= X[i]
      for j in xrange(num_classes):
          dW[:, j] += X[i] * np.exp(scores[j]) /scores_sum

  loss /= num_train  
  #loss += 0.5 * reg * np.sum(W*W)
  dW /= num_train
  loss += reg * np.sum(W * W)
  dW += 2 * reg*W 
        
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  #loss = []
  #dW = []
  num_train = X.shape[0]
  num_classes = W.shape[1]

  scores = np.dot(X, W)
  scores -= scores.max()
  exp_scores = np.exp(scores)
  score_sum = np.sum(exp_scores, axis=1)
  prob = exp_scores[range(num_train), y]
  loss = prob / score_sum
  loss = -np.sum(-np.log(loss))/num_train + reg * np.sum(W *W)


 
   #Gradient

  G = np.divide(exp_scores, score_sum.reshape(num_train, 1))
  G[range(num_train), y] = - (score_sum - prob) / score_sum
  #G = np.equal(y[np.newaxis, :], np.arange(C)[:, np.newaxis]
  dW = X.T.dot(G)
  #dW += np.dot(exp_score.T / norm, X).T

  dW /=num_train
  dW += 2 *reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

