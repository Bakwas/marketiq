#' This is a special R script which can be used to generate a report. You can
#' write normal text in roxygen comments.
#' 
#' First we set up some options (you do not have to do this):

#+ setup, include=FALSE
library(knitr)
opts_chunk$set(fig.path='figure/silk-')

set.seed(123)
twitter_users <- read.csv("TwitterUsers.csv", stringsAsFactors = FALSE)

#' It is usually convenient to cap the max rank to a number.
#' However in the next lines we use the total number of users.
max_rank <- 1000
max_rank <- log(nrow(twitter_users))

#' It makes sense to filter out users who have no followers or tweets to remove bots.
twitter_users <- twitter_users[, ]

hist(twitter_users$Number.of.followers)
hist(log(twitter_users$Number.of.followers + 1))

hist(table(cut(twitter_users$Number.of.friends, breaks = 10)))
hist(log(twitter_users$Number.of.friends + 1))

hist(twitter_users$Tweets)
hist(log(twitter_users$Tweets))

hist(twitter_users$Number.of.retweets)

#' number.of.followers - numfriends + numtweets * numretweets
#' rank <- exp(max_rank * score)
#' convert all values to log except retweets
#' normalize to z-score
#' calculate percentile with pnorm
#' tweet/retweet
#' followers/friends
#' --- remove zero followers and tweets
twitter_users$log_followers <- log(twitter_users$Number.of.followers + 1)
twitter_users$Number.of.followers <- NULL
twitter_users$log_friends <- log(twitter_users$Number.of.friends + 1)
twitter_users$Number.of.friends <- NULL
twitter_users$log_tweets <- log(twitter_users$Tweets + 1)
twitter_users$Tweets <- NULL
twitter_users$log_retweets <- log(twitter_users$Number.of.retweets + 1)
twitter_users$Number.of.retweets <- NULL

twitter_users$log_followers_z <- scale(twitter_users$log_followers)
twitter_users$log_friends_z <- scale(twitter_users$log_friends)
twitter_users$log_tweets_z <- scale(twitter_users$log_tweets)
twitter_users$log_retweets_z <- scale(twitter_users$log_retweets)

twitter_users$log_followers_p <- pnorm(twitter_users$log_followers_z)
twitter_users$log_friends_p <- pnorm(twitter_users$log_friends_z)
twitter_users$log_tweets_p <- pnorm(twitter_users$log_tweets_z)
twitter_users$log_retweets_p <- pnorm(twitter_users$log_retweets_z)

twitter_users$score <- twitter_users$log_followers_p - twitter_users$log_friends_p + twitter_users$log_tweets_p * twitter_users$log_retweets_p
twitter_users$score = (twitter_users$score - min(twitter_users$score)) / (max(twitter_users$score) - min(twitter_users$score))

twitter_users$rank <- exp(max_rank * twitter_users$score)