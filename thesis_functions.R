
### Function to create the dummy variables for the key category 
key.dummy <- function(x){
  x <- x %>% mutate(key1 = ifelse(x$key == 1, 1, 0),
                    key2 = ifelse(x$key == 2, 1, 0),
                    key3 = ifelse(x$key == 3, 1, 0),
                    key4 = ifelse(x$key == 4, 1, 0),
                    key5 = ifelse(x$key == 5, 1, 0),
                    key6 = ifelse(x$key == 6, 1, 0),
                    key7 = ifelse(x$key == 7, 1, 0),
                    key8 = ifelse(x$key == 8, 1, 0),
                    key9 = ifelse(x$key == 9, 1, 0),
                    key10 = ifelse(x$key == 10, 1, 0),
                    key11 = ifelse(x$key == 11, 1, 0)) %>% select(-key)
  
  x
}

#train/valid/test function from data mining class:
partition.3 <- function(data, prop.train, prop.val){
  # select a random sample of size = prop.train % of total records
  selected1 <- sample(1:nrow(data), round(nrow(data)*prop.train), replace = FALSE) 
  # create training data which has prop.train % of total records
  data.train <- data[selected1,]
  # select a random sample of size = prop.val % of the total records
  rest <- setdiff(1:nrow(data), selected1)
  selected2 <- sample(rest, round(nrow(data)*prop.val), replace = FALSE) 
  # create validation data which has prop.val % of total records
  data.val <- data[selected2,]
  # create testing data with the remaining records
  data.test <- data[setdiff(rest, selected2),]
  return(list(data.train=data.train, data.test=data.test, data.val=data.val))
}

### Calculates plots optimal cutoff for the popularity classification
opt.cut.func <- function(model, data){
  # create a vector for cutoff values
  cutoff <- seq(0, 1, 0.01)
  
  # create three empty vectors of same length
  sensitivity.vec <- rep(NA, length(cutoff))
  specificity.vec <- rep(NA, length(cutoff))
  ssdiff.vec <- rep(NA, length(cutoff))
  kappa.vec <- rep(NA, length(cutoff))
  
  # For loop.
  for(i in 1:length(cutoff)){
    pred.prob.val <- predict(model, newdata = data, type = "response")
    pred.y.val <- as.factor(ifelse(pred.prob.val > cutoff[i], 1, 0)) 
    # warning messages galore because the probability of a value actually being popular is SO LOW
    c <- confusionMatrix(pred.y.val, data$popular, 
                         positive = "1")
    sensitivity.vec[i] <- c$byClass["Sensitivity"]
    specificity.vec[i] <- c$byClass["Specificity"]
    ssdiff.vec[i] <- abs(sensitivity.vec[i] - specificity.vec[i])
    kappa.vec[i] <- c$overall["Kappa"]
  }
  return(list(cutoff = cutoff, sensitivity.vec = sensitivity.vec, specificity.vec = specificity.vec, ssdiff.vec = ssdiff.vec, kappa.vec = kappa.vec))
}

reg.opt.cut.func <-  function(model, data){
  cutoff <- seq(0, 1, 0.01)
  
  # create three empty vectors of same length
  sensitivity.vec <- rep(NA, length(cutoff))
  specificity.vec <- rep(NA, length(cutoff))
  ssdiff.vec <- rep(NA, length(cutoff))
  kappa.vec <- rep(NA, length(cutoff))
  
  # For loop.
  for(i in 1:length(cutoff)){
    pred.prob.val <- predict(model, s=model$bestTune, data, type = "prob")
    pred.y.val <- as.factor(ifelse(pred.prob.val[,2] > cutoff[i], 1, 0)) 
    # warning messages galore because the probability of a value actually being popular is SO LOW
    c <- confusionMatrix(pred.y.val, data$popular, 
                         positive = "1")
    sensitivity.vec[i] <- c$byClass["Sensitivity"]
    specificity.vec[i] <- c$byClass["Specificity"]
    ssdiff.vec[i] <- abs(sensitivity.vec[i] - specificity.vec[i])
    kappa.vec[i] <- c$overall["Kappa"]
  }
  return(list(cutoff = cutoff, sensitivity.vec = sensitivity.vec, specificity.vec = specificity.vec, ssdiff.vec = ssdiff.vec, kappa.vec = kappa.vec))
}

### Calculates plots optimal cutoff for the generations classification
opt.cut.gen <- function(model, data){
  # create a vector for cutoff values
  cutoff <- seq(0, 1, 0.01)
  
  # create three empty vectors of same length
  sensitivity.vec <- rep(NA, length(cutoff))
  specificity.vec <- rep(NA, length(cutoff))
  ssdiff.vec <- rep(NA, length(cutoff))
  kappa.vec <- rep(NA, length(cutoff))
  
  # For loop.
  for(i in 1:length(cutoff)){
    pred.prob.val <- predict(model, newdata = data, type = "response")
    pred.y.val <- as.factor(ifelse(pred.prob.val > cutoff[i], 1, 0)) 
    c <- confusionMatrix(pred.y.val, data$oldgen, 
                         positive = "1")
    sensitivity.vec[i] <- c$byClass["Sensitivity"]
    specificity.vec[i] <- c$byClass["Specificity"]
    ssdiff.vec[i] <- abs(sensitivity.vec[i] - specificity.vec[i])
    kappa.vec[i] <- c$overall["Kappa"]
  }
  return(list(cutoff = cutoff, sensitivity.vec = sensitivity.vec, specificity.vec = specificity.vec, ssdiff.vec = ssdiff.vec, kappa.vec = kappa.vec))
}

reg.opt.cut.gen <-  function(model, data){
  cutoff <- seq(0, 1, 0.01)
  
  # create three empty vectors of same length
  sensitivity.vec <- rep(NA, length(cutoff))
  specificity.vec <- rep(NA, length(cutoff))
  ssdiff.vec <- rep(NA, length(cutoff))
  kappa.vec <- rep(NA, length(cutoff))
  
  # For loop.
  for(i in 1:length(cutoff)){
    pred.prob.val <- predict(model, s=model$bestTune, data, type = "prob")
    pred.y.val <- as.factor(ifelse(pred.prob.val[,2] > cutoff[i], 1, 0)) 
    c <- confusionMatrix(pred.y.val, data$oldgen, 
                         positive = "1")
    sensitivity.vec[i] <- c$byClass["Sensitivity"]
    specificity.vec[i] <- c$byClass["Specificity"]
    ssdiff.vec[i] <- abs(sensitivity.vec[i] - specificity.vec[i])
    kappa.vec[i] <- c$overall["Kappa"]
  }
  return(list(cutoff = cutoff, sensitivity.vec = sensitivity.vec, specificity.vec = specificity.vec, ssdiff.vec = ssdiff.vec, kappa.vec = kappa.vec))
}

### Plots the optimal cut off evaluation
opt.cut.plot <- function(opt.out){
  plot(opt.out$cutoff, opt.out$sensitivity.vec,xlab = "cutoff", type = "l", col = "blue")
  lines(opt.out$cutoff, opt.out$specificity.vec, type = "l", col = "green")
  lines(opt.out$cutoff, opt.out$kappa.vec, type = "l", col = "red")
  legend( x="right", legend=c("Sensitivity","Specificity", "Kappa"),
          col=c("blue","green","red"), lty = 1, lwd=1)
  
}

### Applying the box cox transformation
bc.transform <- function(y, lambda){
  t <- (y^(lambda) - 1)/lambda
  return(t)
}