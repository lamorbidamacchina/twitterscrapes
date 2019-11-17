SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `scrapes` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `screen_name` varchar(255) DEFAULT NULL,
  `profile_image_url` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `statuses_count` int(11) DEFAULT NULL,
  `friends_count` int(11) DEFAULT NULL,
  `followers_count` int(11) DEFAULT NULL,
  `account_age_days` int(11) DEFAULT NULL,
  `average_tweets` decimal(10,2) DEFAULT NULL,
  `most_mentioned_users` text DEFAULT NULL,
  `most_used_hashtags` text DEFAULT NULL,
  `processed_tweets` int(11) DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `creation_day` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `scrapes`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `scrapes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;


