-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 21, 2020 at 03:06 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bantaydigital`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'moderator'),
(3, 'editor'),
(4, 'member'),
(5, 'anonymous');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=197 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_user'),
(2, 'Can change user', 1, 'change_user'),
(3, 'Can delete user', 1, 'delete_user'),
(4, 'Can view user', 1, 'view_user'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add site', 7, 'add_site'),
(26, 'Can change site', 7, 'change_site'),
(27, 'Can delete site', 7, 'delete_site'),
(28, 'Can view site', 7, 'view_site'),
(29, 'Can add Token', 8, 'add_token'),
(30, 'Can change Token', 8, 'change_token'),
(31, 'Can delete Token', 8, 'delete_token'),
(32, 'Can view Token', 8, 'view_token'),
(33, 'Can add wyvern custom content', 9, 'add_wyverncustomcontent'),
(34, 'Can change wyvern custom content', 9, 'change_wyverncustomcontent'),
(35, 'Can delete wyvern custom content', 9, 'delete_wyverncustomcontent'),
(36, 'Can view wyvern custom content', 9, 'view_wyverncustomcontent'),
(37, 'Can add wyvern theme', 10, 'add_wyverntheme'),
(38, 'Can change wyvern theme', 10, 'change_wyverntheme'),
(39, 'Can delete wyvern theme', 10, 'delete_wyverntheme'),
(40, 'Can view wyvern theme', 10, 'view_wyverntheme'),
(41, 'Can add wyvern theme config', 11, 'add_wyvernthemeconfig'),
(42, 'Can change wyvern theme config', 11, 'change_wyvernthemeconfig'),
(43, 'Can delete wyvern theme config', 11, 'delete_wyvernthemeconfig'),
(44, 'Can view wyvern theme config', 11, 'view_wyvernthemeconfig'),
(45, 'Can add wyvern module', 12, 'add_wyvernmodule'),
(46, 'Can change wyvern module', 12, 'change_wyvernmodule'),
(47, 'Can delete wyvern module', 12, 'delete_wyvernmodule'),
(48, 'Can view wyvern module', 12, 'view_wyvernmodule'),
(49, 'Can add wyvern module config option', 13, 'add_wyvernmoduleconfigoption'),
(50, 'Can change wyvern module config option', 13, 'change_wyvernmoduleconfigoption'),
(51, 'Can delete wyvern module config option', 13, 'delete_wyvernmoduleconfigoption'),
(52, 'Can view wyvern module config option', 13, 'view_wyvernmoduleconfigoption'),
(53, 'Can add wyvern site', 14, 'add_wyvernsite'),
(54, 'Can change wyvern site', 14, 'change_wyvernsite'),
(55, 'Can delete wyvern site', 14, 'delete_wyvernsite'),
(56, 'Can view wyvern site', 14, 'view_wyvernsite'),
(57, 'Can add wyvern site config', 15, 'add_wyvernsiteconfig'),
(58, 'Can change wyvern site config', 15, 'change_wyvernsiteconfig'),
(59, 'Can delete wyvern site config', 15, 'delete_wyvernsiteconfig'),
(60, 'Can view wyvern site config', 15, 'view_wyvernsiteconfig'),
(61, 'Can add wyvern site config option', 16, 'add_wyvernsiteconfigoption'),
(62, 'Can change wyvern site config option', 16, 'change_wyvernsiteconfigoption'),
(63, 'Can delete wyvern site config option', 16, 'delete_wyvernsiteconfigoption'),
(64, 'Can view wyvern site config option', 16, 'view_wyvernsiteconfigoption'),
(65, 'Can add wyvern site module config', 17, 'add_wyvernsitemoduleconfig'),
(66, 'Can change wyvern site module config', 17, 'change_wyvernsitemoduleconfig'),
(67, 'Can delete wyvern site module config', 17, 'delete_wyvernsitemoduleconfig'),
(68, 'Can view wyvern site module config', 17, 'view_wyvernsitemoduleconfig'),
(69, 'Can add wyvern site modules', 18, 'add_wyvernsitemodules'),
(70, 'Can change wyvern site modules', 18, 'change_wyvernsitemodules'),
(71, 'Can delete wyvern site modules', 18, 'delete_wyvernsitemodules'),
(72, 'Can view wyvern site modules', 18, 'view_wyvernsitemodules'),
(73, 'Can add wyvern post', 19, 'add_wyvernpost'),
(74, 'Can change wyvern post', 19, 'change_wyvernpost'),
(75, 'Can delete wyvern post', 19, 'delete_wyvernpost'),
(76, 'Can view wyvern post', 19, 'view_wyvernpost'),
(77, 'Can add wyvern cart', 20, 'add_wyverncart'),
(78, 'Can change wyvern cart', 20, 'change_wyverncart'),
(79, 'Can delete wyvern cart', 20, 'delete_wyverncart'),
(80, 'Can view wyvern cart', 20, 'view_wyverncart'),
(81, 'Can add wyvern cart item', 21, 'add_wyverncartitem'),
(82, 'Can change wyvern cart item', 21, 'change_wyverncartitem'),
(83, 'Can delete wyvern cart item', 21, 'delete_wyverncartitem'),
(84, 'Can view wyvern cart item', 21, 'view_wyverncartitem'),
(85, 'Can add wyvern inventory', 22, 'add_wyverninventory'),
(86, 'Can change wyvern inventory', 22, 'change_wyverninventory'),
(87, 'Can delete wyvern inventory', 22, 'delete_wyverninventory'),
(88, 'Can view wyvern inventory', 22, 'view_wyverninventory'),
(89, 'Can add wyvern order', 23, 'add_wyvernorder'),
(90, 'Can change wyvern order', 23, 'change_wyvernorder'),
(91, 'Can delete wyvern order', 23, 'delete_wyvernorder'),
(92, 'Can view wyvern order', 23, 'view_wyvernorder'),
(93, 'Can add wyvern order products', 24, 'add_wyvernorderproducts'),
(94, 'Can change wyvern order products', 24, 'change_wyvernorderproducts'),
(95, 'Can delete wyvern order products', 24, 'delete_wyvernorderproducts'),
(96, 'Can view wyvern order products', 24, 'view_wyvernorderproducts'),
(97, 'Can add wyvern payment', 25, 'add_wyvernpayment'),
(98, 'Can change wyvern payment', 25, 'change_wyvernpayment'),
(99, 'Can delete wyvern payment', 25, 'delete_wyvernpayment'),
(100, 'Can view wyvern payment', 25, 'view_wyvernpayment'),
(101, 'Can add wyvern payment method', 26, 'add_wyvernpaymentmethod'),
(102, 'Can change wyvern payment method', 26, 'change_wyvernpaymentmethod'),
(103, 'Can delete wyvern payment method', 26, 'delete_wyvernpaymentmethod'),
(104, 'Can view wyvern payment method', 26, 'view_wyvernpaymentmethod'),
(105, 'Can add wyvern product', 27, 'add_wyvernproduct'),
(106, 'Can change wyvern product', 27, 'change_wyvernproduct'),
(107, 'Can delete wyvern product', 27, 'delete_wyvernproduct'),
(108, 'Can view wyvern product', 27, 'view_wyvernproduct'),
(109, 'Can add wyvern product categories', 28, 'add_wyvernproductcategories'),
(110, 'Can change wyvern product categories', 28, 'change_wyvernproductcategories'),
(111, 'Can delete wyvern product categories', 28, 'delete_wyvernproductcategories'),
(112, 'Can view wyvern product categories', 28, 'view_wyvernproductcategories'),
(113, 'Can add wyvern product category', 29, 'add_wyvernproductcategory'),
(114, 'Can change wyvern product category', 29, 'change_wyvernproductcategory'),
(115, 'Can delete wyvern product category', 29, 'delete_wyvernproductcategory'),
(116, 'Can view wyvern product category', 29, 'view_wyvernproductcategory'),
(117, 'Can add wyvern product config', 30, 'add_wyvernproductconfig'),
(118, 'Can change wyvern product config', 30, 'change_wyvernproductconfig'),
(119, 'Can delete wyvern product config', 30, 'delete_wyvernproductconfig'),
(120, 'Can view wyvern product config', 30, 'view_wyvernproductconfig'),
(121, 'Can add wyvern product type', 31, 'add_wyvernproducttype'),
(122, 'Can change wyvern product type', 31, 'change_wyvernproducttype'),
(123, 'Can delete wyvern product type', 31, 'delete_wyvernproducttype'),
(124, 'Can view wyvern product type', 31, 'view_wyvernproducttype'),
(125, 'Can add wyvern product type config', 32, 'add_wyvernproducttypeconfig'),
(126, 'Can change wyvern product type config', 32, 'change_wyvernproducttypeconfig'),
(127, 'Can delete wyvern product type config', 32, 'delete_wyvernproducttypeconfig'),
(128, 'Can view wyvern product type config', 32, 'view_wyvernproducttypeconfig'),
(129, 'Can add wyvern product type config option', 33, 'add_wyvernproducttypeconfigoption'),
(130, 'Can change wyvern product type config option', 33, 'change_wyvernproducttypeconfigoption'),
(131, 'Can delete wyvern product type config option', 33, 'delete_wyvernproducttypeconfigoption'),
(132, 'Can view wyvern product type config option', 33, 'view_wyvernproducttypeconfigoption'),
(133, 'Can add wyvern shipping address', 34, 'add_wyvernshippingaddress'),
(134, 'Can change wyvern shipping address', 34, 'change_wyvernshippingaddress'),
(135, 'Can delete wyvern shipping address', 34, 'delete_wyvernshippingaddress'),
(136, 'Can view wyvern shipping address', 34, 'view_wyvernshippingaddress'),
(137, 'Can add wyvern shipping method', 35, 'add_wyvernshippingmethod'),
(138, 'Can change wyvern shipping method', 35, 'change_wyvernshippingmethod'),
(139, 'Can delete wyvern shipping method', 35, 'delete_wyvernshippingmethod'),
(140, 'Can view wyvern shipping method', 35, 'view_wyvernshippingmethod'),
(141, 'Can add wyvern shipping provider', 36, 'add_wyvernshippingprovider'),
(142, 'Can change wyvern shipping provider', 36, 'change_wyvernshippingprovider'),
(143, 'Can delete wyvern shipping provider', 36, 'delete_wyvernshippingprovider'),
(144, 'Can view wyvern shipping provider', 36, 'view_wyvernshippingprovider'),
(145, 'Can add wyvern shipping type', 37, 'add_wyvernshippingtype'),
(146, 'Can change wyvern shipping type', 37, 'change_wyvernshippingtype'),
(147, 'Can delete wyvern shipping type', 37, 'delete_wyvernshippingtype'),
(148, 'Can view wyvern shipping type', 37, 'view_wyvernshippingtype'),
(149, 'Can add wyvern jobs', 38, 'add_wyvernjobs'),
(150, 'Can change wyvern jobs', 38, 'change_wyvernjobs'),
(151, 'Can delete wyvern jobs', 38, 'delete_wyvernjobs'),
(152, 'Can view wyvern jobs', 38, 'view_wyvernjobs'),
(153, 'Can add wyvern job applicant', 39, 'add_wyvernjobapplicant'),
(154, 'Can change wyvern job applicant', 39, 'change_wyvernjobapplicant'),
(155, 'Can delete wyvern job applicant', 39, 'delete_wyvernjobapplicant'),
(156, 'Can view wyvern job applicant', 39, 'view_wyvernjobapplicant'),
(157, 'Can add wyvern job categories', 40, 'add_wyvernjobcategories'),
(158, 'Can change wyvern job categories', 40, 'change_wyvernjobcategories'),
(159, 'Can delete wyvern job categories', 40, 'delete_wyvernjobcategories'),
(160, 'Can view wyvern job categories', 40, 'view_wyvernjobcategories'),
(161, 'Can add wyvern job types', 41, 'add_wyvernjobtypes'),
(162, 'Can change wyvern job types', 41, 'change_wyvernjobtypes'),
(163, 'Can delete wyvern job types', 41, 'delete_wyvernjobtypes'),
(164, 'Can view wyvern job types', 41, 'view_wyvernjobtypes'),
(165, 'Can add wyvern employer', 42, 'add_wyvernemployer'),
(166, 'Can change wyvern employer', 42, 'change_wyvernemployer'),
(167, 'Can delete wyvern employer', 42, 'delete_wyvernemployer'),
(168, 'Can view wyvern employer', 42, 'view_wyvernemployer'),
(169, 'Can add wyvern employer jobs', 43, 'add_wyvernemployerjobs'),
(170, 'Can change wyvern employer jobs', 43, 'change_wyvernemployerjobs'),
(171, 'Can delete wyvern employer jobs', 43, 'delete_wyvernemployerjobs'),
(172, 'Can view wyvern employer jobs', 43, 'view_wyvernemployerjobs'),
(173, 'Can add wyvern job application', 44, 'add_wyvernjobapplication'),
(174, 'Can change wyvern job application', 44, 'change_wyvernjobapplication'),
(175, 'Can delete wyvern job application', 44, 'delete_wyvernjobapplication'),
(176, 'Can view wyvern job application', 44, 'view_wyvernjobapplication'),
(177, 'Can add wyvern subscribers', 45, 'add_wyvernsubscribers'),
(178, 'Can change wyvern subscribers', 45, 'change_wyvernsubscribers'),
(179, 'Can delete wyvern subscribers', 45, 'delete_wyvernsubscribers'),
(180, 'Can view wyvern subscribers', 45, 'view_wyvernsubscribers'),
(181, 'Can add wyvern data store', 46, 'add_wyverndatastore'),
(182, 'Can change wyvern data store', 46, 'change_wyverndatastore'),
(183, 'Can delete wyvern data store', 46, 'delete_wyverndatastore'),
(184, 'Can view wyvern data store', 46, 'view_wyverndatastore'),
(185, 'Can add wyvern lms student', 47, 'add_wyvernlmsstudent'),
(186, 'Can change wyvern lms student', 47, 'change_wyvernlmsstudent'),
(187, 'Can delete wyvern lms student', 47, 'delete_wyvernlmsstudent'),
(188, 'Can view wyvern lms student', 47, 'view_wyvernlmsstudent'),
(189, 'Can add wyvern trace log', 48, 'add_wyverntracelog'),
(190, 'Can change wyvern trace log', 48, 'change_wyverntracelog'),
(191, 'Can delete wyvern trace log', 48, 'delete_wyverntracelog'),
(192, 'Can view wyvern trace log', 48, 'view_wyverntracelog'),
(193, 'Can add wyvern medical form', 49, 'add_wyvernmedicalform'),
(194, 'Can change wyvern medical form', 49, 'change_wyvernmedicalform'),
(195, 'Can delete wyvern medical form', 49, 'delete_wyvernmedicalform'),
(196, 'Can view wyvern medical form', 49, 'view_wyvernmedicalform');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-08-20 05:21:01.394327', '1', 'Zan', 3, '', 1, 2),
(2, '2020-08-20 05:21:21.945568', '2', 'WyvernAdmin', 2, '[{\"changed\": {\"fields\": [\"Email\"]}}]', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'wyvernuser', 'user'),
(2, 'admin', 'logentry'),
(3, 'auth', 'permission'),
(4, 'auth', 'group'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'sites', 'site'),
(8, 'authtoken', 'token'),
(9, 'wyverncontent', 'wyverncustomcontent'),
(10, 'wyvernthemes', 'wyverntheme'),
(11, 'wyvernthemes', 'wyvernthemeconfig'),
(12, 'wyvernsite', 'wyvernmodule'),
(13, 'wyvernsite', 'wyvernmoduleconfigoption'),
(14, 'wyvernsite', 'wyvernsite'),
(15, 'wyvernsite', 'wyvernsiteconfig'),
(16, 'wyvernsite', 'wyvernsiteconfigoption'),
(17, 'wyvernsite', 'wyvernsitemoduleconfig'),
(18, 'wyvernsite', 'wyvernsitemodules'),
(19, 'wyvernblog', 'wyvernpost'),
(20, 'wyvernshop', 'wyverncart'),
(21, 'wyvernshop', 'wyverncartitem'),
(22, 'wyvernshop', 'wyverninventory'),
(23, 'wyvernshop', 'wyvernorder'),
(24, 'wyvernshop', 'wyvernorderproducts'),
(25, 'wyvernshop', 'wyvernpayment'),
(26, 'wyvernshop', 'wyvernpaymentmethod'),
(27, 'wyvernshop', 'wyvernproduct'),
(28, 'wyvernshop', 'wyvernproductcategories'),
(29, 'wyvernshop', 'wyvernproductcategory'),
(30, 'wyvernshop', 'wyvernproductconfig'),
(31, 'wyvernshop', 'wyvernproducttype'),
(32, 'wyvernshop', 'wyvernproducttypeconfig'),
(33, 'wyvernshop', 'wyvernproducttypeconfigoption'),
(34, 'wyvernshop', 'wyvernshippingaddress'),
(35, 'wyvernshop', 'wyvernshippingmethod'),
(36, 'wyvernshop', 'wyvernshippingprovider'),
(37, 'wyvernshop', 'wyvernshippingtype'),
(38, 'wyvernjobs', 'wyvernjobs'),
(39, 'wyvernjobs', 'wyvernjobapplicant'),
(40, 'wyvernjobs', 'wyvernjobcategories'),
(41, 'wyvernjobs', 'wyvernjobtypes'),
(42, 'wyvernjobs', 'wyvernemployer'),
(43, 'wyvernjobs', 'wyvernemployerjobs'),
(44, 'wyvernjobs', 'wyvernjobapplication'),
(45, 'wyvernsubscriptions', 'wyvernsubscribers'),
(46, 'wyverndatastorage', 'wyverndatastore'),
(47, 'wyvernlms', 'wyvernlmsstudent'),
(48, 'wyverntrace', 'wyverntracelog'),
(49, 'wyverntrace', 'wyvernmedicalform');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=110 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-08-19 06:12:53.688678'),
(2, 'contenttypes', '0002_remove_content_type_name', '2020-08-19 06:12:54.267347'),
(3, 'auth', '0001_initial', '2020-08-19 06:12:54.809039'),
(4, 'auth', '0002_alter_permission_name_max_length', '2020-08-19 06:12:55.717517'),
(5, 'auth', '0003_alter_user_email_max_length', '2020-08-19 06:12:55.734507'),
(6, 'auth', '0004_alter_user_username_opts', '2020-08-19 06:12:55.750499'),
(7, 'auth', '0005_alter_user_last_login_null', '2020-08-19 06:12:55.769487'),
(8, 'auth', '0006_require_contenttypes_0002', '2020-08-19 06:12:55.774485'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2020-08-19 06:12:55.791479'),
(10, 'auth', '0008_alter_user_username_max_length', '2020-08-19 06:12:55.810464'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2020-08-19 06:12:55.826455'),
(12, 'wyvernuser', '0001_initial', '2020-08-19 06:12:56.016347'),
(13, 'admin', '0001_initial', '2020-08-19 06:12:56.703952'),
(14, 'admin', '0002_logentry_remove_auto_add', '2020-08-19 06:12:56.954814'),
(15, 'admin', '0003_logentry_add_action_flag_choices', '2020-08-19 06:12:56.979798'),
(16, 'auth', '0010_alter_group_name_max_length', '2020-08-19 06:12:57.064746'),
(17, 'auth', '0011_update_proxy_permissions', '2020-08-19 06:12:57.090732'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2020-08-19 06:12:57.115717'),
(19, 'authtoken', '0001_initial', '2020-08-19 06:12:57.215663'),
(20, 'authtoken', '0002_auto_20160226_1747', '2020-08-19 06:12:57.508495'),
(21, 'sessions', '0001_initial', '2020-08-19 06:12:57.619428'),
(22, 'sites', '0001_initial', '2020-08-19 06:12:57.827310'),
(23, 'sites', '0002_alter_domain_unique', '2020-08-19 06:12:57.920256'),
(24, 'wyvernsite', '0001_initial', '2020-08-19 06:12:58.553895'),
(25, 'wyvernblog', '0001_initial', '2020-08-19 06:12:59.959090'),
(26, 'wyvernblog', '0002_auto_20200218_0501', '2020-08-19 06:13:00.161974'),
(27, 'wyvernblog', '0003_auto_20200316_0757', '2020-08-19 06:13:00.661688'),
(28, 'wyvernblog', '0004_auto_20200324_0722', '2020-08-19 06:13:01.018484'),
(29, 'wyvernblog', '0005_auto_20200324_0724', '2020-08-19 06:13:01.792041'),
(30, 'wyvernblog', '0006_auto_20200622_0027', '2020-08-19 06:13:01.876993'),
(31, 'wyvernsite', '0002_wyvernsite_site_owner', '2020-08-19 06:13:01.982935'),
(32, 'wyvernsite', '0003_auto_20200220_0016', '2020-08-19 06:13:02.116858'),
(33, 'wyvernsite', '0004_auto_20200220_0242', '2020-08-19 06:13:02.715514'),
(34, 'wyvernsite', '0005_auto_20200310_0206', '2020-08-19 06:13:02.755489'),
(35, 'wyvernsite', '0006_auto_20200317_1531', '2020-08-19 06:13:02.793468'),
(36, 'wyvernsite', '0007_auto_20200319_0443', '2020-08-19 06:13:02.893412'),
(37, 'wyvernsite', '0008_auto_20200324_0722', '2020-08-19 06:13:03.338156'),
(38, 'wyvernsite', '0009_auto_20200324_0726', '2020-08-19 06:13:03.698950'),
(39, 'wyvernsite', '0010_wyvernsite_site_favicon', '2020-08-19 06:13:03.793895'),
(40, 'wyvernsite', '0011_auto_20200324_1211', '2020-08-19 06:13:03.833873'),
(41, 'wyvernsite', '0012_auto_20200327_1245', '2020-08-19 06:13:03.959800'),
(42, 'wyvernsite', '0013_auto_20200327_1320', '2020-08-19 06:13:04.002776'),
(43, 'wyvernsite', '0014_wyvernsite_site_redirect', '2020-08-19 06:13:04.106716'),
(44, 'wyverncontent', '0001_initial', '2020-08-19 06:13:04.210657'),
(45, 'wyverncontent', '0002_auto_20200707_1410', '2020-08-19 06:13:04.541468'),
(46, 'wyverndatastorage', '0001_initial', '2020-08-19 06:13:04.649407'),
(47, 'wyverndatastorage', '0002_auto_20200427_0541', '2020-08-19 06:13:04.860289'),
(48, 'wyverndatastorage', '0003_auto_20200427_0542', '2020-08-19 06:13:04.899264'),
(49, 'wyvernjobs', '0001_initial', '2020-08-19 06:13:04.986213'),
(50, 'wyvernjobs', '0002_auto_20200218_0501', '2020-08-19 06:13:05.201091'),
(51, 'wyvernjobs', '0003_wyvernjobs_job_type', '2020-08-19 06:13:05.469938'),
(52, 'wyvernjobs', '0004_wyvernjobapplicant_wyvernjobcategories_wyvernjobtypes', '2020-08-19 06:13:06.084592'),
(53, 'wyvernjobs', '0005_auto_20200313_0331', '2020-08-19 06:13:07.799605'),
(54, 'wyvernjobs', '0006_auto_20200323_0618', '2020-08-19 06:13:09.443664'),
(55, 'wyvernjobs', '0007_auto_20200323_0627', '2020-08-19 06:13:09.550603'),
(56, 'wyvernjobs', '0008_auto_20200323_0819', '2020-08-19 06:13:09.798459'),
(57, 'wyvernjobs', '0009_auto_20200323_0836', '2020-08-19 06:13:10.040321'),
(58, 'wyvernjobs', '0010_auto_20200323_0837', '2020-08-19 06:13:10.112280'),
(59, 'wyvernjobs', '0011_wyvernjobapplication_job_application_applicant_info', '2020-08-19 06:13:10.258196'),
(60, 'wyvernjobs', '0012_remove_wyvernjobapplication_job_application_applicant_info', '2020-08-19 06:13:10.616991'),
(61, 'wyvernjobs', '0013_wyvernjobs_job_location', '2020-08-19 06:13:10.778902'),
(62, 'wyvernjobs', '0014_wyvernjobs_job_frequency', '2020-08-19 06:13:10.941805'),
(63, 'wyvernjobs', '0015_auto_20200324_1535', '2020-08-19 06:13:11.009768'),
(64, 'wyvernjobs', '0016_auto_20200324_1600', '2020-08-19 06:13:11.313592'),
(65, 'wyvernjobs', '0017_auto_20200325_0144', '2020-08-19 06:13:11.614421'),
(66, 'wyvernjobs', '0018_auto_20200601_0339', '2020-08-19 06:13:11.737352'),
(67, 'wyvernjobs', '0019_auto_20200603_0241', '2020-08-19 06:13:11.862279'),
(68, 'wyvernjobs', '0020_auto_20200603_0315', '2020-08-19 06:13:12.075158'),
(69, 'wyvernjobs', '0021_auto_20200605_0006', '2020-08-19 06:13:12.258052'),
(70, 'wyvernjobs', '0022_auto_20200610_0952', '2020-08-19 06:13:12.768762'),
(71, 'wyvernjobs', '0023_auto_20200610_0956', '2020-08-19 06:13:12.923671'),
(72, 'wyvernjobs', '0024_auto_20200610_1004', '2020-08-19 06:13:12.996629'),
(73, 'wyvernjobs', '0025_wyvernjobapplication_job_application_applicant_user', '2020-08-19 06:13:13.147547'),
(74, 'wyvernjobs', '0026_wyvernjobapplicant_job_applicant_additional_form', '2020-08-19 06:13:13.358423'),
(75, 'wyvernjobs', '0027_remove_wyvernjobapplicant_job_applicant_introduction', '2020-08-19 06:13:13.499342'),
(76, 'wyvernjobs', '0028_auto_20200622_0027', '2020-08-19 06:13:13.611281'),
(77, 'wyvernjobs', '0018_auto_20200511_0535', '2020-08-19 06:13:13.857137'),
(78, 'wyvernjobs', '0029_merge_20200803_0432', '2020-08-19 06:13:13.868131'),
(79, 'wyvernjobs', '0030_auto_20200803_0435', '2020-08-19 06:13:14.203938'),
(80, 'wyvernlms', '0001_initial', '2020-08-19 06:13:14.381837'),
(81, 'wyvernlms', '0002_auto_20200622_2342', '2020-08-19 06:13:14.868558'),
(82, 'wyvernlms', '0003_auto_20200622_2343', '2020-08-19 06:13:15.004483'),
(83, 'wyvernlms', '0004_auto_20200622_2350', '2020-08-19 06:13:15.303309'),
(84, 'wyvernlms', '0005_auto_20200622_2351', '2020-08-19 06:13:15.464219'),
(85, 'wyvernlms', '0006_auto_20200705_0209', '2020-08-19 06:13:15.754051'),
(86, 'wyvernshop', '0001_initial', '2020-08-19 06:13:17.613987'),
(87, 'wyvernshop', '0002_auto_20200218_0501', '2020-08-19 06:13:17.954792'),
(88, 'wyvernshop', '0003_auto_20200218_0501', '2020-08-19 06:13:23.862413'),
(89, 'wyvernsite', '0015_auto_20200809_0347', '2020-08-19 06:13:26.625831'),
(90, 'wyvernsubscriptions', '0001_initial', '2020-08-19 06:13:26.868695'),
(91, 'wyvernsubscriptions', '0002_wyvernsubscibers_sub_email', '2020-08-19 06:13:27.297449'),
(92, 'wyvernsubscriptions', '0003_auto_20200302_0752', '2020-08-19 06:13:27.410382'),
(93, 'wyvernsubscriptions', '0004_auto_20200302_0833', '2020-08-19 06:13:27.657240'),
(94, 'wyvernthemes', '0001_initial', '2020-08-19 06:13:28.279885'),
(95, 'wyvernthemes', '0002_auto_20200327_1136', '2020-08-19 06:13:28.792591'),
(96, 'wyvernthemes', '0003_auto_20200327_1145', '2020-08-19 06:13:28.929514'),
(97, 'wyvernthemes', '0004_auto_20200327_1147', '2020-08-19 06:13:29.142390'),
(98, 'wyvernthemes', '0005_auto_20200327_2344', '2020-08-19 06:13:29.957923'),
(99, 'wyvernthemes', '0006_auto_20200327_2348', '2020-08-19 06:13:30.201787'),
(100, 'wyvernthemes', '0007_wyvernthemeconfig_wyverntheme_google_fonts', '2020-08-19 06:13:30.383680'),
(101, 'wyvernthemes', '0008_auto_20200601_0349', '2020-08-19 06:13:30.703497'),
(102, 'wyvernthemes', '0009_wyvernthemeconfig_wyverntheme_page_layout', '2020-08-19 06:13:30.914381'),
(103, 'wyvernthemes', '0010_auto_20200616_0309', '2020-08-19 06:13:31.072286'),
(104, 'wyvernthemes', '0011_auto_20200803_0435', '2020-08-19 06:13:31.550013'),
(105, 'wyverntrace', '0001_initial', '2020-08-19 06:13:31.751897'),
(106, 'wyverntrace', '0002_wyvernmedicalform', '2020-08-19 06:13:32.049726'),
(107, 'wyvernuser', '0002_auto_20200803_0435', '2020-08-19 06:13:32.860264'),
(108, 'wyvernuser', '0003_user_uuid', '2020-08-19 06:13:33.051154'),
(109, 'wyvernuser', '0004_auto_20200819_1412', '2020-08-19 06:13:33.795727');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `wyvernblog_wyvernpost`
--

DROP TABLE IF EXISTS `wyvernblog_wyvernpost`;
CREATE TABLE IF NOT EXISTS `wyvernblog_wyvernpost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_title` varchar(255) NOT NULL,
  `post_slug` varchar(255) DEFAULT NULL,
  `post_type` varchar(100) NOT NULL,
  `post_content` longtext,
  `post_thumbnail` varchar(100) DEFAULT NULL,
  `post_custom_template` varchar(255) DEFAULT NULL,
  `post_carousel` varchar(255) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `post_author_id` int(11) NOT NULL,
  `post_site_id` int(11) NOT NULL,
  `post_description` longtext,
  `post_keywords` varchar(255) DEFAULT NULL,
  `post_seo_author` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyvernblog_wyvernpost_post_slug_4d92ac2e_uniq` (`post_slug`),
  KEY `wyvernblog_wyvernpost_post_site_id_94b79911` (`post_site_id`),
  KEY `wyvernblog_wyvernpost_post_author_id_a18409b6` (`post_author_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyverncontent_wyverncustomcontent`
--

DROP TABLE IF EXISTS `wyverncontent_wyverncustomcontent`;
CREATE TABLE IF NOT EXISTS `wyverncontent_wyverncustomcontent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wyvern_custom_content_label` varchar(255) DEFAULT NULL,
  `wyvern_custom_content_content` longtext,
  `wyvern_custom_content_image` varchar(100) DEFAULT NULL,
  `wyvern_custom_content_site_id` int(11) NOT NULL,
  `wyvern_custom_content_slug` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyverncontent_wyverncustomc_wyvern_custom_content_site__1e91234f` (`wyvern_custom_content_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyverndatastorage_wyverndatastore`
--

DROP TABLE IF EXISTS `wyverndatastorage_wyverndatastore`;
CREATE TABLE IF NOT EXISTS `wyverndatastorage_wyverndatastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_store_identity` varchar(255) DEFAULT NULL,
  `data_store_content` longtext,
  `data_store_tags` longtext,
  `data_store_timestamp` datetime(6) NOT NULL,
  `data_store_status` int(11) NOT NULL,
  `data_store_site_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyverndatastorage_wyverndatastore_data_store_site_id_26347106` (`data_store_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernemployer`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernemployer`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernemployer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_employer_title` longtext,
  `job_employer_company_name` longtext,
  `job_employer_company_image` varchar(100) DEFAULT NULL,
  `job_employer_site_id` int(11) NOT NULL,
  `job_employer_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernemployer_job_employer_site_id_01d9c291` (`job_employer_site_id`),
  KEY `wyvernjobs_wyvernemployer_job_employer_user_id_0260ef54` (`job_employer_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernemployerjobs`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernemployerjobs`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernemployerjobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_employer_jobs_employer_id` int(11) NOT NULL,
  `job_employer_jobs_job_id` int(11) NOT NULL,
  `job_employer_jobs_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernemployerjo_job_employer_jobs_employer__bb64ebac` (`job_employer_jobs_employer_id`),
  KEY `wyvernjobs_wyvernemployerjobs_job_employer_jobs_job_id_2c8c5295` (`job_employer_jobs_job_id`),
  KEY `wyvernjobs_wyvernemployerjobs_job_employer_jobs_site_id_3c62711e` (`job_employer_jobs_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernjobapplicant`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernjobapplicant`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernjobapplicant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_applicant_user_id` int(11) DEFAULT NULL,
  `job_applicant_site_id` int(11) NOT NULL,
  `job_applicant_title` varchar(255) DEFAULT NULL,
  `job_applicant_resume` varchar(100) DEFAULT NULL,
  `job_applicant_email` varchar(255) DEFAULT NULL,
  `job_applicant_number` varchar(255) DEFAULT NULL,
  `job_applicant_firstname` varchar(255) DEFAULT NULL,
  `job_applicant_lastname` varchar(255) DEFAULT NULL,
  `job_applicant_additional_form` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernjobapplicant_job_application_site_id_b8c31595` (`job_applicant_site_id`),
  KEY `wyvernjobs_wyvernjobapplicant_job_applicant_user_id_06c27f07` (`job_applicant_user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wyvernjobs_wyvernjobapplicant`
--

INSERT INTO `wyvernjobs_wyvernjobapplicant` (`id`, `job_applicant_user_id`, `job_applicant_site_id`, `job_applicant_title`, `job_applicant_resume`, `job_applicant_email`, `job_applicant_number`, `job_applicant_firstname`, `job_applicant_lastname`, `job_applicant_additional_form`) VALUES
(1, 3, 1, NULL, '', NULL, NULL, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernjobapplication`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernjobapplication`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernjobapplication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_application_applicant_id` int(11) DEFAULT NULL,
  `job_application_job_id` int(11) NOT NULL,
  `job_application_site_id` int(11) NOT NULL,
  `job_application_cover_letter` longtext,
  `job_application_applicant_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernjobapplica_job_application_applicant_i_a60bfad9` (`job_application_applicant_id`),
  KEY `wyvernjobs_wyvernjobapplication_job_application_job_id_f9ded9e8` (`job_application_job_id`),
  KEY `wyvernjobs_wyvernjobapplication_job_application_site_id_41d7e024` (`job_application_site_id`),
  KEY `wyvernjobs_wyvernjobapplica_job_application_applicant_u_a4163ce7` (`job_application_applicant_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernjobcategories`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernjobcategories`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernjobcategories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_category_title` varchar(255) NOT NULL,
  `job_category_description` longtext,
  `job_category_short_description` varchar(255) DEFAULT NULL,
  `job_category_slug` varchar(255) DEFAULT NULL,
  `job_category_image` varchar(100) DEFAULT NULL,
  `job_category_status` int(11) NOT NULL,
  `job_category_content` longtext,
  `date_created` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `job_category_parent_id` int(11) DEFAULT NULL,
  `job_category_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernjobcategories_created_by_id_dde187ff` (`created_by_id`),
  KEY `wyvernjobs_wyvernjobcategories_job_category_parent_id_2f17743e` (`job_category_parent_id`),
  KEY `wyvernjobs_wyvernjobcategories_job_category_site_id_191b4a31` (`job_category_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernjobs`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernjobs`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernjobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_title` varchar(255) NOT NULL,
  `job_description` longtext,
  `job_subtitle` varchar(255) DEFAULT NULL,
  `job_slug` varchar(255) DEFAULT NULL,
  `job_image` varchar(100) DEFAULT NULL,
  `job_status` int(11) NOT NULL,
  `job_content` longtext,
  `job_notifications_recipients` varchar(255) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `job_posted_by_id` int(11) NOT NULL,
  `job_site_id` int(11) NOT NULL,
  `job_type` varchar(100) NOT NULL,
  `job_location` varchar(255) NOT NULL,
  `job_hours` varchar(100) NOT NULL,
  `job_experience_required` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyvernjobs_wyvernjobs_job_slug_e8417b0f_uniq` (`job_slug`),
  KEY `wyvernjobs_wyvernjobs_job_posted_by_id_1fac3073` (`job_posted_by_id`),
  KEY `wyvernjobs_wyvernjobs_job_site_id_4ce3baf3` (`job_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernjobs_wyvernjobtypes`
--

DROP TABLE IF EXISTS `wyvernjobs_wyvernjobtypes`;
CREATE TABLE IF NOT EXISTS `wyvernjobs_wyvernjobtypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_type_title` varchar(255) NOT NULL,
  `job_type_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernjobs_wyvernjobtypes_job_type_site_id_b096fde2` (`job_type_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernlms_wyvernlmsstudent`
--

DROP TABLE IF EXISTS `wyvernlms_wyvernlmsstudent`;
CREATE TABLE IF NOT EXISTS `wyvernlms_wyvernlmsstudent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wyvernlms_firstname` varchar(255) NOT NULL,
  `wyvernlms_middlename` varchar(255) NOT NULL,
  `wyvernlms_lastname` varchar(255) NOT NULL,
  `wyvernlms_birthdate` datetime(6) DEFAULT NULL,
  `wyvernlms_gender` varchar(255) DEFAULT NULL,
  `wyvernlms_email_address` varchar(255) DEFAULT NULL,
  `wyvernlms_mobile_number` varchar(255) DEFAULT NULL,
  `wyvernlms_wyvern_site_id` int(11) DEFAULT NULL,
  `wyvernlms_wyvern_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyvernlms_email_address` (`wyvernlms_email_address`),
  UNIQUE KEY `wyvernlms_mobile_number` (`wyvernlms_mobile_number`),
  KEY `wyvernlms_wyvernlmsstudent_wyvernlms_wyvern_site_id_bdfced62` (`wyvernlms_wyvern_site_id`),
  KEY `wyvernlms_wyvernlmsstudent_wyvernlms_wyvern_user_id_50430e80` (`wyvernlms_wyvern_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyverncart`
--

DROP TABLE IF EXISTS `wyvernshop_wyverncart`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyverncart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_status` varchar(10) NOT NULL,
  `cart_total_currency` varchar(3) NOT NULL,
  `cart_total` decimal(14,2) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `cart_customer_id` int(11) NOT NULL,
  `cart_site_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyverncart_cart_customer_id_f7639156` (`cart_customer_id`),
  KEY `wyvernshop_wyverncart_cart_site_id_23412df9` (`cart_site_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wyvernshop_wyverncart`
--

INSERT INTO `wyvernshop_wyverncart` (`id`, `cart_status`, `cart_total_currency`, `cart_total`, `date_created`, `cart_customer_id`, `cart_site_id`) VALUES
(1, 'current', 'USD', '0.00', '2020-08-20 05:23:42.311104', 2, NULL),
(2, 'current', 'USD', '0.00', '2020-08-20 07:36:45.587924', 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyverncartitem`
--

DROP TABLE IF EXISTS `wyvernshop_wyverncartitem`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyverncartitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_product_quantity` int(11) NOT NULL,
  `cart_sub_total_currency` varchar(3) NOT NULL,
  `cart_sub_total` decimal(14,2) NOT NULL,
  `cart_cart_id` int(11) NOT NULL,
  `cart_product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyverncartitem_cart_cart_id_d8d4d8bc` (`cart_cart_id`),
  KEY `wyvernshop_wyverncartitem_cart_product_id_ef5350ec` (`cart_product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyverninventory`
--

DROP TABLE IF EXISTS `wyvernshop_wyverninventory`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyverninventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inventory_quantity` int(11) NOT NULL,
  `inventory_unit` varchar(255) NOT NULL,
  `inventory_unit_type` varchar(10) NOT NULL,
  `inventory_product_id` int(11) NOT NULL,
  `inventory_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyverninventory_inventory_product_id_bd502bf6` (`inventory_product_id`),
  KEY `wyvernshop_wyverninventory_inventory_site_id_b0373968` (`inventory_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernorder`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernorder`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` datetime(6) NOT NULL,
  `order_amount_currency` varchar(3) NOT NULL,
  `order_amount` decimal(14,2) NOT NULL,
  `order_status` varchar(25) NOT NULL,
  `order_address_id` int(11) NOT NULL,
  `order_cart_id` int(11) DEFAULT NULL,
  `order_customer_id` int(11) NOT NULL,
  `order_payment_method_id` int(11) DEFAULT NULL,
  `order_shipping_method_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernorder_order_address_id_06626af2` (`order_address_id`),
  KEY `wyvernshop_wyvernorder_order_cart_id_0b650276` (`order_cart_id`),
  KEY `wyvernshop_wyvernorder_order_customer_id_e7b85339` (`order_customer_id`),
  KEY `wyvernshop_wyvernorder_order_payment_method_id_f2412629` (`order_payment_method_id`),
  KEY `wyvernshop_wyvernorder_order_shipping_method_id_f2e61848` (`order_shipping_method_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernorderproducts`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernorderproducts`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernorderproducts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_quantity` int(11) NOT NULL,
  `order_amount_currency` varchar(3) NOT NULL,
  `order_amount` decimal(14,2) NOT NULL,
  `order_product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernorderproducts_order_product_id_9e625cac` (`order_product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernpayment`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernpayment`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernpayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `payment_amount_currency` varchar(3) NOT NULL,
  `payment_amount` decimal(14,2) NOT NULL,
  `payment_status` varchar(10) NOT NULL,
  `payment_customer_id` int(11) NOT NULL,
  `payment_method_id` int(11) NOT NULL,
  `payment_order_id` int(11) NOT NULL,
  `payment_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernpayment_payment_customer_id_7b417210` (`payment_customer_id`),
  KEY `wyvernshop_wyvernpayment_payment_method_id_c6bd1e8e` (`payment_method_id`),
  KEY `wyvernshop_wyvernpayment_payment_order_id_13be7f46` (`payment_order_id`),
  KEY `wyvernshop_wyvernpayment_payment_site_id_babf36e4` (`payment_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernpaymentmethod`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernpaymentmethod`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernpaymentmethod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `payment_method_name` varchar(255) NOT NULL,
  `payment_method_provider` varchar(255) NOT NULL,
  `payment_method_description` longtext,
  `payment_method_instructions` longtext,
  `payment_method_configuration` longtext,
  `payment_method_enabled` tinyint(1) NOT NULL,
  `payment_method_site_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernpaymentmethod_payment_method_site_id_e6331b0d` (`payment_method_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproduct`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproduct`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_image` varchar(100) DEFAULT NULL,
  `product_alt_image_1` varchar(100) DEFAULT NULL,
  `product_alt_image_2` varchar(100) DEFAULT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_sub_text` varchar(255) NOT NULL,
  `product_weight` varchar(255) DEFAULT NULL,
  `product_description` longtext,
  `product_code` varchar(255) DEFAULT NULL,
  `product_slug` varchar(255) DEFAULT NULL,
  `product_sku` varchar(255) DEFAULT NULL,
  `product_price_currency` varchar(3) NOT NULL,
  `product_price` decimal(14,2) NOT NULL,
  `product_enabled` tinyint(1) NOT NULL,
  `product_content` longtext,
  `product_short_description` longtext,
  `product_featured_image` varchar(100) DEFAULT NULL,
  `product_site_id` int(11) NOT NULL,
  `product_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_slug` (`product_slug`),
  KEY `wyvernshop_wyvernproduct_product_site_id_33e1424a` (`product_site_id`),
  KEY `wyvernshop_wyvernproduct_product_type_id_7b64f9cf` (`product_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproductcategories`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproductcategories`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproductcategories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_created` datetime(6) NOT NULL,
  `product_categories_category_id` int(11) NOT NULL,
  `product_categories_product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernproductcat_product_categories_category_cdea87b8` (`product_categories_category_id`),
  KEY `wyvernshop_wyvernproductcat_product_categories_product__416ac427` (`product_categories_product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproductcategory`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproductcategory`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproductcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_category_image` varchar(100) DEFAULT NULL,
  `product_category_featured_image` varchar(100) DEFAULT NULL,
  `product_category_name` varchar(255) NOT NULL,
  `product_category_sub_text` varchar(255) DEFAULT NULL,
  `product_category_slug` varchar(255) DEFAULT NULL,
  `product_category_description` longtext,
  `product_category_content` longtext,
  `date_created` datetime(6) NOT NULL,
  `product_category_site_id` int(11) NOT NULL,
  `product_parent_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_category_slug` (`product_category_slug`),
  KEY `wyvernshop_wyvernproductcat_product_category_site_id_f0a66dac` (`product_category_site_id`),
  KEY `wyvernshop_wyvernproductcat_product_parent_category_id_47630e5b` (`product_parent_category_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproductconfig`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproductconfig`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproductconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_config_option_id` int(11) NOT NULL,
  `product_config_option_value_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernproductconfig_product_config_option_id_ac1c48f5` (`product_config_option_id`),
  KEY `wyvernshop_wyvernproductcon_product_config_option_value_c6e5a089` (`product_config_option_value_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproducttype`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproducttype`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproducttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type_name` varchar(255) NOT NULL,
  `product_type_description` longtext,
  `product_type_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernproducttype_product_type_site_id_b59c69e5` (`product_type_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproducttypeconfig`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproducttypeconfig`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproducttypeconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type_config_name` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `product_type_config_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernproducttyp_product_type_config_type_id_cda0b734` (`product_type_config_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernproducttypeconfigoption`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernproducttypeconfigoption`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernproducttypeconfigoption` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type_config_option_value` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `product_type_config_option_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernproducttyp_product_type_config_option__c3d64301` (`product_type_config_option_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernshippingaddress`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernshippingaddress`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernshippingaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_address_first_name` varchar(255) NOT NULL,
  `shipping_address_last_name` varchar(255) NOT NULL,
  `shipping_address_contact_no` varchar(255) NOT NULL,
  `shipping_address_email_notifications` varchar(255) NOT NULL,
  `shipping_address_address_line_1` varchar(255) NOT NULL,
  `shipping_address_address_line_2` varchar(255) DEFAULT NULL,
  `shipping_address_city` varchar(255) NOT NULL,
  `shipping_address_state` varchar(255) DEFAULT NULL,
  `shipping_address_country` varchar(2) NOT NULL,
  `shipping_address_postcode` varchar(255) NOT NULL,
  `shipping_address_default` tinyint(1) NOT NULL,
  `shipping_address_customer_id` int(11) NOT NULL,
  `shipping_address_site_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernshippingad_shipping_address_customer_i_dca09e55` (`shipping_address_customer_id`),
  KEY `wyvernshop_wyvernshippingad_shipping_address_site_id_53ad1c9c` (`shipping_address_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernshippingmethod`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernshippingmethod`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernshippingmethod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_method_name` varchar(255) NOT NULL,
  `shipping_method_description` longtext,
  `shipping_method_cost_currency` varchar(3) NOT NULL,
  `shipping_method_cost` decimal(14,2) NOT NULL,
  `shipping_method_enabled` tinyint(1) NOT NULL,
  `shipping_method_site_id` int(11) DEFAULT NULL,
  `shipping_method_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernshop_wyvernshippingmethod_shipping_method_site_id_1fcd32e8` (`shipping_method_site_id`),
  KEY `wyvernshop_wyvernshippingmethod_shipping_method_type_id_e3edbf1e` (`shipping_method_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernshippingprovider`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernshippingprovider`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernshippingprovider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_provider_name` varchar(255) NOT NULL,
  `shipping_provider_website` longtext,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernshop_wyvernshippingtype`
--

DROP TABLE IF EXISTS `wyvernshop_wyvernshippingtype`;
CREATE TABLE IF NOT EXISTS `wyvernshop_wyvernshippingtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_method_type_name` varchar(255) NOT NULL,
  `shipping_method_type_provider` varchar(255) NOT NULL,
  `shipping_method_type_description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernmodule`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernmodule`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernmodule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(255) NOT NULL,
  `module_slug` varchar(50) NOT NULL,
  `module_description` longtext NOT NULL,
  `module_status` int(11) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernmoduleconfigoption`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernmoduleconfigoption`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernmoduleconfigoption` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_config_option_name` varchar(20) NOT NULL,
  `module_config_option_validation` longtext,
  `module_config_option_values` longtext,
  `module_config_option_default` longtext,
  `date_created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernsite`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernsite`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernsite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_url` varchar(255) NOT NULL,
  `site_name` varchar(255) NOT NULL,
  `site_analytics` varchar(255) DEFAULT NULL,
  `site_subtitle` varchar(255) DEFAULT NULL,
  `site_logo` varchar(100) DEFAULT NULL,
  `site_status` int(11) NOT NULL,
  `site_type` varchar(10) NOT NULL,
  `site_template` varchar(50) NOT NULL,
  `site_notifications_recipients` varchar(255) DEFAULT NULL,
  `site_notifications_from` varchar(255) DEFAULT NULL,
  `site_description` longtext,
  `date_created` datetime(6) NOT NULL,
  `site_owner_id` int(11) NOT NULL,
  `site_address` longtext,
  `site_email` varchar(255) DEFAULT NULL,
  `site_google_map` longtext,
  `site_logo_dark` varchar(100) DEFAULT NULL,
  `site_number` varchar(255) DEFAULT NULL,
  `site_number_alt` varchar(255) DEFAULT NULL,
  `site_addthis` varchar(255) DEFAULT NULL,
  `site_fb_admins` varchar(255) DEFAULT NULL,
  `site_google_verification` varchar(255) DEFAULT NULL,
  `site_recaptcha` varchar(255) DEFAULT NULL,
  `site_favicon` varchar(100) DEFAULT NULL,
  `site_meta_image` varchar(100) DEFAULT NULL,
  `site_redirect` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_url` (`site_url`),
  KEY `wyvernsite_wyvernsite_site_owner_id_f70e9452` (`site_owner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wyvernsite_wyvernsite`
--

INSERT INTO `wyvernsite_wyvernsite` (`id`, `site_url`, `site_name`, `site_analytics`, `site_subtitle`, `site_logo`, `site_status`, `site_type`, `site_template`, `site_notifications_recipients`, `site_notifications_from`, `site_description`, `date_created`, `site_owner_id`, `site_address`, `site_email`, `site_google_map`, `site_logo_dark`, `site_number`, `site_number_alt`, `site_addthis`, `site_fb_admins`, `site_google_verification`, `site_recaptcha`, `site_favicon`, `site_meta_image`, `site_redirect`) VALUES
(1, 'trace.local:8000', 'Trace', NULL, 'Bantay Digital', 'users/images/80e48d5c-bdb6-4425-adce-5d3c8318f350.png', 1, 'hybrid', 'basic', NULL, NULL, '', '2020-08-20 05:31:53.006296', 2, '', NULL, '', 'users/images/a44514f1-842f-4506-b522-d5d44abe822d.png', NULL, NULL, NULL, NULL, NULL, NULL, 'users/images/6825c098-70b7-4c1f-a302-c6d26c252981.jpg', 'users/images/2e1a52ef-6495-43be-8f78-1834d6803934.jpg', '/trace/dashboard/');

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernsiteconfig`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernsiteconfig`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernsiteconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `config_value` longtext,
  `date_created` datetime(6) NOT NULL,
  `config_name_id` int(11) NOT NULL,
  `config_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernsite_wyvernsiteconfig_config_name_id_7998cd12` (`config_name_id`),
  KEY `wyvernsite_wyvernsiteconfig_config_site_id_869e61e8` (`config_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernsiteconfigoption`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernsiteconfigoption`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernsiteconfigoption` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_config_option_name` varchar(20) NOT NULL,
  `site_config_option_validation` longtext,
  `site_config_option_values` longtext,
  `site_config_option_default` longtext,
  `date_created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernsitemoduleconfig`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernsitemoduleconfig`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernsitemoduleconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_module_config_value` longtext,
  `site_module_config_module_id` int(11) NOT NULL,
  `site_module_config_name_id` int(11) NOT NULL,
  `site_module_config_site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernsite_wyvernsitemodule_site_module_config_module_i_9500a64e` (`site_module_config_module_id`),
  KEY `wyvernsite_wyvernsitemodule_site_module_config_name_id_5f8bd11e` (`site_module_config_name_id`),
  KEY `wyvernsite_wyvernsitemodule_site_module_config_site_id_da201af6` (`site_module_config_site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsite_wyvernsitemodules`
--

DROP TABLE IF EXISTS `wyvernsite_wyvernsitemodules`;
CREATE TABLE IF NOT EXISTS `wyvernsite_wyvernsitemodules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_module_status` int(11) NOT NULL,
  `date_active` datetime(6) NOT NULL,
  `site_id` int(11) NOT NULL,
  `site_module_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernsite_wyvernsitemodules_site_id_24781039` (`site_id`),
  KEY `wyvernsite_wyvernsitemodules_site_module_id_ab6a280b` (`site_module_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernsubscriptions_wyvernsubscribers`
--

DROP TABLE IF EXISTS `wyvernsubscriptions_wyvernsubscribers`;
CREATE TABLE IF NOT EXISTS `wyvernsubscriptions_wyvernsubscribers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_firstname` varchar(255) DEFAULT NULL,
  `sub_lastname` varchar(255) DEFAULT NULL,
  `sub_fullname` varchar(255) DEFAULT NULL,
  `sub_status` int(11) NOT NULL,
  `sub_date` datetime(6) NOT NULL,
  `sub_site_id` int(11) DEFAULT NULL,
  `subscriber_id` int(11) DEFAULT NULL,
  `sub_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyvernsubscriptions_wyvernsubscibers_sub_site_id_c140b29e` (`sub_site_id`),
  KEY `wyvernsubscriptions_wyvernsubscibers_subscriber_id_f5cc3442` (`subscriber_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernthemes_wyverntheme`
--

DROP TABLE IF EXISTS `wyvernthemes_wyverntheme`;
CREATE TABLE IF NOT EXISTS `wyvernthemes_wyverntheme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wyverntheme_name` varchar(255) NOT NULL,
  `wyverntheme_slug` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyverntheme_name` (`wyverntheme_name`),
  UNIQUE KEY `wyverntheme_slug` (`wyverntheme_slug`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernthemes_wyvernthemeconfig`
--

DROP TABLE IF EXISTS `wyvernthemes_wyvernthemeconfig`;
CREATE TABLE IF NOT EXISTS `wyvernthemes_wyvernthemeconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wyverntheme_index_template` varchar(255) DEFAULT NULL,
  `wyverntheme_site_id` int(11) DEFAULT NULL,
  `wyverntheme_custom_css` longtext,
  `wyverntheme_custom_js` longtext,
  `wyverntheme_theme_id` int(11) DEFAULT NULL,
  `wyverntheme_google_fonts` longtext,
  `wyverntheme_footer_template` varchar(255) DEFAULT NULL,
  `wyverntheme_header_template` varchar(255) DEFAULT NULL,
  `wyverntheme_base_layout` varchar(255) DEFAULT NULL,
  `wyverntheme_back_to_top` tinyint(1) NOT NULL,
  `wyverntheme_gdpr` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyverntheme_theme_id` (`wyverntheme_theme_id`),
  UNIQUE KEY `wyvernthemes_wyvernthemeconfig_wyverntheme_site_id_9947d51f_uniq` (`wyverntheme_site_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wyvernthemes_wyvernthemeconfig`
--

INSERT INTO `wyvernthemes_wyvernthemeconfig` (`id`, `wyverntheme_index_template`, `wyverntheme_site_id`, `wyverntheme_custom_css`, `wyverntheme_custom_js`, `wyverntheme_theme_id`, `wyverntheme_google_fonts`, `wyverntheme_footer_template`, `wyverntheme_header_template`, `wyverntheme_base_layout`, `wyverntheme_back_to_top`, `wyverntheme_gdpr`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0),
(2, 'themes/trace/pages/landing.html', 1, 'themes/trace/css/custom.css', '', NULL, '', NULL, NULL, 'themes/trace/base/trace-base.html', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `wyverntrace_wyvernmedicalform`
--

DROP TABLE IF EXISTS `wyverntrace_wyvernmedicalform`;
CREATE TABLE IF NOT EXISTS `wyverntrace_wyvernmedicalform` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyverntrace_wyverntracelog`
--

DROP TABLE IF EXISTS `wyverntrace_wyverntracelog`;
CREATE TABLE IF NOT EXISTS `wyverntrace_wyverntracelog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wyvern_temperature` varchar(255) DEFAULT NULL,
  `wyvern_trace_date` datetime(6) NOT NULL,
  `wyvern_location_id` int(11) DEFAULT NULL,
  `wyvern_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wyverntrace_wyverntracelog_wyvern_location_id_ddb5fc09` (`wyvern_location_id`),
  KEY `wyverntrace_wyverntracelog_wyvern_user_id_7e5afb91` (`wyvern_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wyvernuser_user`
--

DROP TABLE IF EXISTS `wyvernuser_user`;
CREATE TABLE IF NOT EXISTS `wyvernuser_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `about` longtext,
  `dateofbirth` datetime(6) NOT NULL,
  `hometown` varchar(255) DEFAULT NULL,
  `location` longtext,
  `geolocation` longtext,
  `facebook` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `interests` longtext,
  `groups_id` int(11) DEFAULT NULL,
  `address` longtext,
  `is_location` tinyint(1) NOT NULL,
  `phone` varchar(17) DEFAULT NULL,
  `site_id` int(11) DEFAULT NULL,
  `uuid` varchar(100),
  `accepted_terms` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `wyvernuser_user_uuid_5e542045_uniq` (`uuid`),
  KEY `wyvernuser_user_groups_id_112521db` (`groups_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wyvernuser_user`
--

INSERT INTO `wyvernuser_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`, `image`, `about`, `dateofbirth`, `hometown`, `location`, `geolocation`, `facebook`, `website`, `gender`, `interests`, `groups_id`, `address`, `is_location`, `phone`, `site_id`, `uuid`, `accepted_terms`) VALUES
(3, 'pbkdf2_sha256$216000$pyRpf2DpZS0M$2RWZseGIK+Bzf2b6TF5IdyWaFSi6g7vafNi82lQhixo=', '2020-08-21 02:22:58.350693', 0, 'zanrouck.gamad@gmail.com', 'Zan Rouck', 'Gamad', 0, 1, '2020-08-20 07:36:42.251790', 'zanrouck.gamad@gmail.com', '', NULL, '2020-08-20 07:36:43.887770', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'asdasdaad', 0, '09672113497', NULL, '60b2f988-a7b3-41f5-8268-8629b9871d9b', 1),
(2, 'pbkdf2_sha256$216000$bCaXiFra9jyu$MKXXHNmVxx5Yr1Jw7DnJh79KbgBDWbArHxag0LZHsCU=', '2020-08-21 02:39:19.014746', 1, 'WyvernAdmin', '', '', 1, 1, '2020-08-20 05:14:28.000000', 'dummyzan@gmail.com', '', '', '2020-08-20 05:14:29.101656', NULL, '', '', NULL, NULL, NULL, '', 1, '', 0, NULL, NULL, '88c6fb52-fcb2-4352-ae34-414f7e2083ff', 0);

-- --------------------------------------------------------

--
-- Table structure for table `wyvernuser_user_user_permissions`
--

DROP TABLE IF EXISTS `wyvernuser_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `wyvernuser_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wyvernuser_user_user_per_user_id_permission_id_08398b7d_uniq` (`user_id`,`permission_id`),
  KEY `wyvernuser_user_user_permissions_user_id_63b45860` (`user_id`),
  KEY `wyvernuser_user_user_permissions_permission_id_d9f4196d` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
